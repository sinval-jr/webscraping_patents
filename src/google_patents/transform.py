import pandas as pd
import json
import os # Boa prática para verificar se o arquivo existe

# Supondo que list_patents seja preenchido como no seu exemplo
# list_patents = pd.read_csv('patents/Patents - Página1.csv')['publication_number'].tolist()

# --- PARA FINS DE TESTE (usando seu JSON de exemplo) ---
# Vamos simular o ambiente para que o código funcione
list_patents = pd.read_csv('patents/Patents - Página1.csv')['publication_number'].tolist()
    #publication_number = "CN111909735A" 

all_patents_data = []
all_citations_data = []

# Loop principal para iterar sobre cada número de publicação
for e, publication_number in enumerate(list_patents):
    filename = f"patents/{publication_number}.json"

    # Usar try/except é uma boa prática para caso o arquivo não exista
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Carrega o JSON do arquivo. 'patent_data' é um dicionário
            patent_data = json.load(f)

        # Guarda o publication_number principal para usar na tabela de citações
        main_pub_number = patent_data.get('publication_number')
        
        # Se o arquivo JSON não tiver um 'publication_number', pulamos ele
        if not main_pub_number:
            print(f"Aviso: Arquivo {filename} não tem 'publication_number'. Pulando.")
            continue

        # --- TABELA 1: Informações da Patente ---
        patent_info = {
            "publication_number": main_pub_number,
            "title": patent_data.get('title'),
            "assignee_original": patent_data.get('assignee_original'),
            "assignee_current": patent_data.get('assignee_current'),
            "country_name": patent_data.get('country_name'),
            "abstract": patent_data.get('abstract')
        }
        all_patents_data.append(patent_info)

        # --- TABELA 2: Informações das Citações ---
        # Pega a lista de citações (ou uma lista vazia, se 'citations' não existir)
        citations_list = patent_data.get('citations', [])
        
        if citations_list: # Garante que a lista não é None ou vazia
            # Loop aninhado: para cada citação DENTRO da lista de citações
            for citation in citations_list:
                citation_info = {
                    # Coluna 1: O ID da patente principal (para ligação)
                    "publication_number": main_pub_number, 
                    
                    # Colunas 2-6: Dados da citação
                    "citation_publication_number": citation.get('publication_number'),
                    "citation_priority_date": citation.get('priority_date'),
                    "citation_publication_date": citation.get('publication_date'),
                    "citation_assignee": citation.get('assignee'),
                    "citation_title": citation.get('title')
                }
                all_citations_data.append(citation_info)
        
    except FileNotFoundError:
        print(f"Aviso: Arquivo não encontrado: {filename}")
    except json.JSONDecodeError:
        print(f"Aviso: Erro ao ler o JSON do arquivo: {filename}")
    except Exception as ex:
        print(f"Erro inesperado ao processar {filename}: {ex}")


# --- Fim do Loop ---
# Agora, criamos os DataFrames a partir das listas

print("\n--- Processamento concluído. Gerando DataFrames... ---")

# Tabela 1: Patentes
df_patents = pd.DataFrame(all_patents_data)

# Tabela 2: Citações
df_citations = pd.DataFrame(all_citations_data)

# Renomeia as colunas da Tabela 2 para o formato exato que você pediu
df_citations = df_citations.rename(columns={
    "citation_publication_number": "citation[publication_number]",
    "citation_priority_date": "citation[priority_date]",
    "citation_publication_date": "citation[publication_date]",
    "citation_assignee": "citation[assignee]",
    "citation_title": "citation[title]"
})

# --- Exibe os resultados ---

print("\n✅ TABELA 1 (Patentes):")
print(df_patents)
df_patents.to_csv('patents_summary.csv', index=False)  # Salva a Tabela 1 em CSV

print("\n✅ TABELA 2 (Citações):")
print(df_citations)
df_citations.to_csv('patent_citations.csv', index=False)  # Salva a Tabela 2 em CSV

        