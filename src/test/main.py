import pandas as pd
import datetime
from google.cloud import bigquery
from google.oauth2 import service_account

def create_bigquery_client():
    credentials = service_account.Credentials.from_service_account_file(
        filename='GBQ.json', 
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client


def configure_and_execute_dry_run(query: str, client: bigquery.Client):

    # DRY RUN | Estimativa de Custo
    job_config = bigquery.QueryJobConfig(dry_run=True)

    print("Executando 'Dry Run' para estimar o custo...")
    dry_run_job = client.query(query, job_config=job_config)
    bytes_estimate = dry_run_job.total_bytes_processed
    gb_estimate = bytes_estimate / (1024 ** 3)

    print(f"ESTIMATIVA DA CONSULTA: {gb_estimate:.4f} GB")

def created_query_job(query: str, client: bigquery.Client, arq: str):
    print("Executando a consulta no BigQuery...")
    query_job = client.query(query)  
    results = query_job.result()
    print("Consulta concluída. Iniciando download.")

    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")
    output_file = f'data/{arq}_{data_formatada}.csv'
    is_first_chunk = True
    print(f"Iniciando o download e salvamento em '{output_file}'...")

    for chunk_df in results.to_dataframe_iterable():
        if is_first_chunk:
            chunk_df.to_csv(output_file, index=False, mode='w')
            is_first_chunk = False
            print("Primeiro bloco salvo (com cabeçalho)...")
        else:
            chunk_df.to_csv(output_file, index=False, mode='a', header=False)
            print("Mais um bloco anexado...")

    print("\n--- Download e salvamento concluídos! ---")
    return query_job

def information_costs(query_job: bigquery.QueryJob):
    print("\n--- Informações de Custo da Consulta ---")

    # Verifique os detalhes do job concluído
    if query_job.total_bytes_processed is not None:
        gb_processed = query_job.total_bytes_processed / (1024 ** 3)
        print(f"Dados Processados: {gb_processed:.4f} GB")
    else:
        print("Dados Processados: 0 B (provavelmente usou o cache)")

    if query_job.total_bytes_billed is not None:
        gb_billed = query_job.total_bytes_billed / (1024 ** 3)
        print(f"Dados Faturados: {gb_billed:.4f} GB")
    else:
        print("Dados Faturados: 0 B")

    print(f"Resultado veio do Cache: {query_job.cache_hit}")

    print("--------------------------------------\n")

def created_query():
    start_date = '20200101'
    end_date = '20201231'
    query = f'''
            SELECT
            t.publication_number,
            t.priority_date,
            t.`ipc`[SAFE_OFFSET(0)].code AS ipc_code
            FROM
            `patents-public-data.patents.publications` AS t
            WHERE
                t.priority_date BETWEEN {start_date} AND {end_date}
                AND
                EXISTS (
                    SELECT 1 
                    FROM UNNEST(t.ipc) AS ipc_code  
                    WHERE ipc_code.code = 'B23D45/14' 
                )
            LIMIT 1000
    '''
    return query

def verification_consumption():
    query = '''
        SELECT
        creation_time,
        job_id,
        user_email,
        total_bytes_billed,
        query
        FROM
        `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
        WHERE
        creation_time BETWEEN TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), MONTH) AND CURRENT_TIMESTAMP()
        AND job_type = 'QUERY'
        AND state = 'DONE'
        ORDER BY
        creation_time DESC;
    '''
    return query

if __name__ == "__main__":
    print("Iniciando o BigQuery Client...")
    client = create_bigquery_client()
    print("Client iniciado com sucesso.")
    while True:
        print("\nOpções:")
        print("1. Verificar consumo")
        print("2. Solicitar dados ao BigQuery")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            query = verification_consumption()
            arq = 'bq_consumo'
            query_job = created_query_job(query, client, arq)
            information_costs(query_job)
        elif choice == '2':
            #Filtros

            query = created_query()
            arq = 'bq_patents'
            configure_and_execute_dry_run(query, client)
            print("Deseja prosseguir com a execução da consulta? (s/n)")
            proceed = input().lower()
            if proceed != 's':
                print("Consulta cancelada pelo usuário.")
                continue
            query_job = created_query_job(query, client, arq)
            information_costs(query_job)

        elif choice == '0':
            print("Saindo...")
            break
