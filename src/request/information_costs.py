from google.cloud import bigquery



def information_costs(query_job: bigquery.QueryJob):
    """Exibe informações de custo da consulta, como dados processados, faturados e se o resultado veio do cache."""
    print("\n--- Informações de Custo da Consulta ---")

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