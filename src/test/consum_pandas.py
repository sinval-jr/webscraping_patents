import pandas as pd

df = pd.read_csv('data/bq_consumo_20251127_074332.csv')
print(df.head())
print(f"\nNúmero total de registros: {len(df)}")

total_bytes = df['total_bytes_billed'].sum()
total_gb = total_bytes / (1024 ** 3)
print(f"\nTotal de bytes faturados no mês atual: {total_bytes} bytes ({total_gb:.4f} GB)")


