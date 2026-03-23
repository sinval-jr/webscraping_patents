import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import datetime
from pathlib import Path

caminho_atual = Path(__file__).resolve()
diretorio_acima = caminho_atual.parent.parent
caminho_arquivo = diretorio_acima / "GBQ.json"

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


def configure_and_execute_dry_run(query: str, client: bigquery.Client):

    # DRY RUN | Estimativa de Custo
    job_config = bigquery.QueryJobConfig(dry_run=True)

    print("Executando 'Dry Run' para estimar o custo...")
    dry_run_job = client.query(query, job_config=job_config)
    # A execução do dry run não processará os dados, mas fornecerá uma estimativa do custo
    bytes_estimate = dry_run_job.total_bytes_processed
    gb_estimate = bytes_estimate / (1024 ** 3)

    print(f"ESTIMATIVA DA CONSULTA: {gb_estimate:.4f} GB")

def created_query_job(query: str, client: bigquery.Client, arq: str):
    print("Executando a consulta no BigQuery...")
    # A execução real da consulta processará os dados e retornará os resultados
    query_job = client.query(query)  
    results = query_job.result()
    print("Consulta concluída. Iniciando download.")

    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")
    output_file = f'{arq}_{data_formatada}.csv'
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

arq = 'bq_patents_citations'
# Consulta SQL para obter as patentes principais e as patentes citadas
query = '''
SELECT 
  t1.publication_number AS patente_principal, 
  citacao.publication_number AS patente_citada
FROM 
  `patents-public-data.google_patents_research.publications` AS t1,
  UNNEST(t1.cited_by) AS citacao 
LIMIT 1000
'''
# Configuração de credenciais e cliente BigQuery
credentials = service_account.Credentials.from_service_account_file(filename = 'GBQ.json', 
                                                                    scopes = ["https://www.googleapis.com/auth/cloud-platform"])

client = bigquery.Client(credentials=credentials, project=credentials.project_id)


configure_and_execute_dry_run(query, client)
print("Deseja prosseguir com a execução da consulta? (s/n)")
proceed = input().lower()
if proceed != 's':
    print("Consulta cancelada pelo usuário.")
    exit()

query_job = created_query_job(query, client, arq)
information_costs(query_job)
print("Data saved to patents_data_citations.csv")