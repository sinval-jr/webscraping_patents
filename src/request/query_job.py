from google.cloud import bigquery
import datetime

def created_query_job(query: str, client: bigquery.Client):
    """Executa a consulta no BigQuery, salva os resultados em um arquivo CSV e retorna o objeto QueryJob para análise posterior."""
    arq = 'data/bq_patents_'
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