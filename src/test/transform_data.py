import pandas as pd

df = pd.read_csv('data/bq_patents_verifica_campos - bq_patents_verifica_campos.csv')

colunas_interessadas = ['assignee_harmonized', 'all_citations_detailed']
df_filtrado = df[colunas_interessadas]
print(df_filtrado.head())