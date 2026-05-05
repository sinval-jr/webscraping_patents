from google.cloud import bigquery
import datetime
from src.data.load_data import process_and_save_data

def created_query_job(query: str, client: bigquery.Client, arq: str, campos_por_fonte: dict, ):
    """Executa a consulta no BigQuery, salva os resultados em um arquivo CSV e retorna o objeto QueryJob para análise posterior."""
    print("Executando a consulta no BigQuery...")
    # A execução real da consulta processará os dados e retornará os resultados
    query_job = client.query(query)  
    results = query_job.result()
    print("Consulta concluída. Iniciando download.")

    # Processa os dados iterativamente salvando em arquivos CSV separados de acordo com as fontes/dicionários
    process_and_save_data(results, campos_por_fonte)

    print("\n--- Download e salvamento concluídos! ---")
    return query_job