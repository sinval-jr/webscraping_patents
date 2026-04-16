import pandas as pd
import datetime

def transform_data_citation(df: pd.DataFrame) -> pd.DataFrame:
    df = df[['patente_principal', 'patente_citada']]
    df.drop_duplicates(inplace=True)
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")
    output_file = f'patent_citation_{data_formatada}.csv'
    return df, output_file

def transform_data_center(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['patente_citada'])
    df.drop_duplicates(inplace=True)
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%Y%m%d_%H%M%S")
    output_file = f'patent_{data_formatada}.csv'
    return df, output_file

    
