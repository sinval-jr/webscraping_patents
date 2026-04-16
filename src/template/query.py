
dict_campos_t1 ={
    "publication_number": "t1.publication_number AS publication_number",
    'title': 't1.title as title',
    'title_translated': 't1.title_translated as title_translated',
    'abstract': 't1.abstract as abstract',
    'abstract_translated': 't1.abstract_translated as abstract_translated',
    'cpc_low': 't1.cpc_low as cpc_low',
    'cpc_inventive_low': 't1.cpc_inventive_low as cpc_inventive_low',
    'top_terms': 't1.top_terms as top_terms',
    'url': 't1.url as url',
    'country': 't1.country as country',
    'publication_description': 't1.publication_description as publication_description',
    'embeddings_v1': 't1.embeddings_v1 as embeddings_v1',
}

dict_campos_cpc = {
    'cpc_code': 'cpc.code as cpc_code',
    'cpc_inventive': 'cpc.inventive as cpc_inventive',
    'cpc_first': 'cpc.first as cpc_first',
    'cpc_tree': 'cpc.tree as cpc_tree',
}

dict_campos_similar = {
    'similar_publication_number': 'similar.publication_number as similar_publication_number',
    'similar_application_number': 'similar.application_number as similar_application_number',
    'similar_npl_text': 'similar.first as similar_first',
    'similar_type': 'similar.tree as similar_type',
    'similar_category': 'similar.tree as category',
    'similar_filling_data': 'similar.filling_data as similar_filling_data',
}

dict_campos_cited_by = {
    'cited_by_publication_number': 'cited.publication_number as cited_by_publication_number',
    'cited_by_application_number': 'cited.application_number as cited_by_application_number',
    'cited_by_npl_text': 'cited.first as cited_by_npl_text',
    'cited_by_type': 'cited.tree as cited_by_type',
    'cited_by_category': 'cited.tree as cited_by_category',
    'cited_by_filling_data': 'cited.filling_data as cited_by_filling_data',
}

dict_from ={
    't1': '`patents-public-data.google_patents_research.publications` AS t1',
    'cpc': 'UNNEST(t1.cpc) AS cpc',
    'similar': 'UNNEST(t1.similar) AS similar',
    'cited_by': 'UNNEST(t1.cited_by) AS cited',
}

def gerar_query_patents(campos_desejados, limit=10000):
    # Agrupa todos os mapeamentos de campos
    todos_campos = {
        **dict_campos_t1, 
        **dict_campos_cpc, 
        **dict_campos_similar, 
        **dict_campos_cited_by
    }
    
    # 1. Identifica as cláusulas SELECT
    select_clauses = [todos_campos[campo] for campo in campos_desejados if campo in todos_campos]
    
    # 2. Identifica quais fontes (FROM/UNNEST) são necessárias
    # Sempre incluímos a t1 (tabela principal)
    fontes_necessarias = ['t1']
    
    for campo in campos_desejados:
        if campo in dict_campos_cpc:
            fontes_necessarias.append('cpc')
        elif campo in dict_campos_similar:
            fontes_necessarias.append('similar')
        elif campo in dict_campos_cited_by:
            fontes_necessarias.append('cited_by')
            
    from_clauses = [dict_from[fonte] for fonte in fontes_necessarias]

    # 3. Monta a String final
    query = "SELECT\n    "
    query += ",\n    ".join(select_clauses)
    query += "\nFROM\n    "
    query += ",\n    ".join(from_clauses)
    query += f"\nLIMIT {limit}"
    
    return query

# --- Exemplo de Uso ---

# Escolha as chaves que você quer extrair (conforme definido nos seus dicts)
def print_campos_disponiveis():
    print("Campos de tabela principal (t1):")
    for key in dict_campos_t1.keys():
        print(f"- {key}")
    print("Campos de tabela CPC (cpc):")
    for key in dict_campos_cpc.keys():
        print(f"- {key}")
    print("Campos de tabela Similar (similar):")
    for key in dict_campos_similar.keys():
        print(f"- {key}")
    print("Campos de tabela Cited By (cited_by):")
    for key in dict_campos_cited_by.keys():
        print(f"- {key}")

def print_limites_disponiveis():
    print("Limites disponíveis:")
    print("1. - 1000")
    print("2. - 5000")
    print("3. - 10000")
    
