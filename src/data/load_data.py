import pandas as pd
import datetime

def process_and_save_data(results, campos_por_fonte: dict):
    """
    Processa os resultados da consulta de forma genérica, criando tabelas diferentes
    de acordo com as fontes requisitadas (campos_por_fonte), removendo dados duplicados
    entre todos os chunks (não só dentro de cada um).
    """
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")

    output_files = {fonte: f'patent_{fonte}_{data_formatada}.csv' for fonte in campos_por_fonte}
    header_written = {fonte: False for fonte in campos_por_fonte}
    # ponytail: set em memória por fonte — ok para os limites atuais (até ~10k ou
    # "sem limite" de um dataset filtrado); se volumes crescerem muito, trocar por
    # dedup incremental em disco/DB.
    seen_keys = {fonte: set() for fonte in campos_por_fonte}

    for chunk_df in results.to_dataframe_iterable():
        for fonte, campos in campos_por_fonte.items():

            colunas_fonte = [col for col in campos if col in chunk_df.columns]

            if fonte != 't1' and 'publication_number' in chunk_df.columns and 'publication_number' not in colunas_fonte:
                colunas_fonte.insert(0, 'publication_number')

            if not colunas_fonte:
                continue

            df_fonte = chunk_df[colunas_fonte].copy()
            df_fonte.drop_duplicates(inplace=True)

            keys = list(df_fonte.itertuples(index=False, name=None))
            is_new = [key not in seen_keys[fonte] for key in keys]
            seen_keys[fonte].update(key for key, novo in zip(keys, is_new) if novo)
            df_fonte = df_fonte[is_new]

            if df_fonte.empty:
                continue

            if not header_written[fonte]:
                df_fonte.to_csv(output_files[fonte], index=False, mode='w')
                header_written[fonte] = True
            else:
                df_fonte.to_csv(output_files[fonte], index=False, mode='a', header=False)

        print("Bloco processado (duplicados entre chunks removidos)...")
