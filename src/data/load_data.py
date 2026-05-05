import pandas as pd
import datetime

def process_and_save_data(results, campos_por_fonte: dict):
    """
    Processa os resultados da consulta de forma genérica, criando tabelas diferentes
    de acordo com as fontes requisitadas (campos_por_fonte), removendo dados duplicados.
    """
    is_first_chunk = True
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")
    
    output_files = {}
    for fonte in campos_por_fonte.keys():
        output_files[fonte] = f'patent_{fonte}_{data_formatada}.csv'
        
    for chunk_df in results.to_dataframe_iterable():
        for fonte, campos in campos_por_fonte.items():
            # Filtra apenas as colunas que estão presentes no dataframe retornado
            colunas_fonte = [col for col in campos if col in chunk_df.columns]
            
            # Adicionar a chave primária 'publication_number' para tabelas que não sejam a t1
            # Isso é importante para conseguirmos fazer o JOIN depois
            if fonte != 't1' and 'publication_number' in chunk_df.columns and 'publication_number' not in colunas_fonte:
                colunas_fonte.insert(0, 'publication_number')
                
            if not colunas_fonte:
                continue
                
            # Cria DataFrame com as colunas da fonte e remove os duplicados
            df_fonte = chunk_df[colunas_fonte].copy()
            df_fonte.drop_duplicates(inplace=True)
            
            # Salva no arquivo CSV correspondente
            if is_first_chunk:
                df_fonte.to_csv(output_files[fonte], index=False, mode='w')
            else:
                df_fonte.to_csv(output_files[fonte], index=False, mode='a', header=False)
                
        if is_first_chunk:
            print("Primeiro bloco salvo (com cabeçalho) para todas as fontes...")
            is_first_chunk = False
        else:
            print("Mais um bloco anexado para todas as fontes...")