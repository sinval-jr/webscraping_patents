from google.cloud import bigquery
import datetime
from src.data.load_data import process_and_save_data

def created_query_job(query: str, client: bigquery.Client, arq: str, campos_por_fonte: dict, ):
    """Executa a consulta no BigQuery, salva os resultados em um arquivo CSV e retorna o objeto QueryJob para análise posterior."""
    print("Executando a consulta no BigQuery...")
    # Cria o dataset temporário se não existir
    dataset_id = f"{client.project}.temp_dataset"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    try:
        client.create_dataset(dataset)
        print(f"Dataset '{dataset_id}' criado.")
    except Exception:
        pass  # Dataset já existe

    job_config = bigquery.QueryJobConfig(
        allow_large_results=True,
        destination=f"{dataset_id}.temp_{arq}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
    )
    query_job = client.query(query, job_config=job_config)  
    results = query_job.result()
    print("Consulta concluída. Iniciando download.")

    process_and_save_data(results, campos_por_fonte)

    print("\n--- Download e salvamento concluídos! ---")
    return query_job