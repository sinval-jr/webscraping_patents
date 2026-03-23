from google.cloud import bigquery

def configure_and_execute_dry_run(query: str, client: bigquery.Client):

    """Executa um "Dry Run" para estimar o custo da consulta sem processar os dados."""
    job_config = bigquery.QueryJobConfig(dry_run=True)

    print("Executando 'Dry Run' para estimar o custo...")
    dry_run_job = client.query(query, job_config=job_config)

    bytes_estimate = dry_run_job.total_bytes_processed
    gb_estimate = bytes_estimate / (1024 ** 3)

    print(f"ESTIMATIVA DA CONSULTA: {gb_estimate:.4f} GB")