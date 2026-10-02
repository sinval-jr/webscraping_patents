from google.cloud import bigquery
from src.data.load_data import process_and_save_data

def created_query_job(query: str, client: bigquery.Client, campos_por_fonte: dict, query_parameters=None):
    """Executa a consulta no BigQuery, salva os resultados em um arquivo CSV e retorna o objeto QueryJob para análise posterior."""
    print("Executando a consulta no BigQuery...")
    # Sem destino explícito, o BigQuery usa uma tabela temporária gerenciada por ele
    # mesmo (expira em ~24h sozinha) — não precisamos criar/limpar dataset nenhum.
    job_config = bigquery.QueryJobConfig(query_parameters=query_parameters or [])
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()
    print("Consulta concluída. Iniciando download.")

    process_and_save_data(results, campos_por_fonte)

    print("\n--- Download e salvamento concluídos! ---")
    return query_job