import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# 1. Configuração da Consulta
query = '''
    SELECT publication_number, priority_date, grant_date 
    FROM `patents-public-data.patents.publications`
    LIMIT 1000
'''
# 2. Autenticação e Cliente BigQuery
credentials = service_account.Credentials.from_service_account_file(
    filename='GBQ.json', 
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
# Criação do Cliente BigQuery
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# ETAPA 1: CONFIGURAR E EXECUTAR O "DRY RUN"
job_config = bigquery.QueryJobConfig(dry_run=True)

print("Executando 'Dry Run' para estimar o custo...")

# Isso NÃO executa a consulta, apenas a valida e estima o custo.
# É instantâneo e gratuito.
dry_run_job = client.query(query, job_config=job_config)

# Obtenha os bytes processados da simulação
bytes_estimate = dry_run_job.total_bytes_processed
gb_estimate = bytes_estimate / (1024 ** 3)

print(f"ESTIMATIVA DA CONSULTA: {gb_estimate:.4f} GB")


print("Executando a consulta no BigQuery...")
query_job = client.query(query)  

print("Aguardando a consulta ser concluída no BigQuery...")
results = query_job.result()
print("Consulta concluída. Iniciando download.")

output_file = 'data/bq_catálago_patents_completo.csv'
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
