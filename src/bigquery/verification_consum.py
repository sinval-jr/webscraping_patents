import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account# 1. Configuração da Consulta

#Precisa de permissão para acessar o INFORMATION_SCHEMA.JOBS_BY_PROJECT (Usuário do BigQuery e  Leitor de recursos do BigQuery)
query = '''
    SELECT
    creation_time,
    job_id,
    user_email,
    total_bytes_billed,
    (total_bytes_billed / POWER(1024, 3)) AS gb_billed,
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
#`liquid-engine-474717-i6`.`region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
# 2. Autenticação e Cliente BigQuery
credentials = service_account.Credentials.from_service_account_file(
    filename='GBQ.json', 
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
# Criação do Cliente BigQuery
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

print("Executando a consulta no BigQuery...")
query_job = client.query(query)  

print("Aguardando a consulta ser concluída no BigQuery...")
results = query_job.result()
print("Consulta concluída. Iniciando download.")

output_file = 'data/bq_consumo.csv'
is_first_chunk = True
print(f"Iniciando o download e salvamento em '{output_file}'...")

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