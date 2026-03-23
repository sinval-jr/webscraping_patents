import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account



# Consulta
query = '''
    SELECT
        t.publication_number,
        t.priority_date,
    FROM
        `patents-public-data.patents.publications` AS t
    LIMIT 1000
'''
# 2. Autenticação e Cliente BigQuery
credentials = service_account.Credentials.from_service_account_file(
    filename='GBQ.json', 
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# DRY RUN | Estimativa de Custo
job_config = bigquery.QueryJobConfig(dry_run=True)

print("Executando 'Dry Run' para estimar o custo...")
dry_run_job = client.query(query, job_config=job_config)
bytes_estimate = dry_run_job.total_bytes_processed
gb_estimate = bytes_estimate / (1024 ** 3)

print(f"ESTIMATIVA DA CONSULTA: {gb_estimate:.4f} GB")

# Execução da Consulta

print("Executando a consulta no BigQuery...")
query_job = client.query(query)  

print("Aguardando a consulta ser concluída no BigQuery...")
results = query_job.result()
print("Consulta concluída. Iniciando download.")

output_file = 'data/bq_patents_verifica_campos.csv'
is_first_chunk = True
print(f"Iniciando o download e salvamento em '{output_file}'...")

print("Aqui é o resultado do dataframe iterable:")
print(results)

for chunk_df in results.to_dataframe_iterable():
    if is_first_chunk:
        # No primeiro pedaço, escreva o cabeçalho e sobrescreva o arquivo
        chunk_df.to_csv(output_file, index=False, mode='w')
        is_first_chunk = False
        print("Primeiro bloco salvo (com cabeçalho)...")
    else:
        # Nos pedaços seguintes, anexe (append) os dados sem o cabeçalho
        chunk_df.to_csv(output_file, index=False, mode='a', header=False)
        print("Mais um bloco anexado...")

print("\n--- Download e salvamento concluídos! ---")


#df = query_job.to_dataframe()

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
