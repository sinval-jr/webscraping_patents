from transformer import transform_data_citation, transform_data_center

def load_data_citation(results):
    """Processa os resultados da consulta, salva os dados transformados em arquivos CSV e retorna o objeto QueryJob para análise posterior."""
    is_first_chunk = True

    for chunk_df in results.to_dataframe_iterable():
        citation_df, output_citation = transform_data_citation(chunk_df)
        center_df, output_center = transform_data_center(chunk_df)
        if is_first_chunk:
            citation_df.to_csv(output_citation, index=False, mode='w')
            center_df.to_csv(output_center, index=False, mode='w')
            is_first_chunk = False
            print("Primeiro bloco salvo (com cabeçalho)...")
        else:
            citation_df.to_csv(output_citation, index=False, mode='a', header=False)
            center_df.to_csv(output_center, index=False, mode='a', header=False)
            print("Mais um bloco anexado...")

def load_data(results):
    """Processa os resultados da consulta, salva os dados transformados em arquivos CSV e retorna o objeto QueryJob para análise posterior."""
    is_first_chunk = True

    for chunk_df in results.to_dataframe_iterable():
        center_df, output_center = transform_data_center(chunk_df)
        if is_first_chunk:
            center_df.to_csv(output_center, index=False, mode='w')
            is_first_chunk = False
            print("Primeiro bloco salvo (com cabeçalho)...")
        else:
            center_df.to_csv(output_center, index=False, mode='a', header=False)
            print("Mais um bloco anexado...")