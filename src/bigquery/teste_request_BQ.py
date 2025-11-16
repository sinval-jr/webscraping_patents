import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# 1. Configuração (exatamente como o seu)
query = '''
    SELECT 
        publication_number, 
        priority_date, 
        assignee, 
        `citation`[SAFE_OFFSET(0)] 
    FROM 
        `patents-public-data.patents.publications` 
    LIMIT 1000
'''

credentials = service_account.Credentials.from_service_account_file(
    filename='GBQ.json', 
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id)

print("Executando a consulta no BigQuery...")
query_job = client.query(query)  


df = query_job.to_dataframe()

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



print(df.head())
df.to_csv('patents_data_2.csv', index=False)
print("\nDados salvos em patents_data.csv")