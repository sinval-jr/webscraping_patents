
def input_filters():
    print("_______Defina os Filtros da Consulta (Pressione Enter para pular)_______")
    filters = {}
    
    filters['priority_date'] = input("Data de Prioridade (Ex exata: 20200101 ou período: 20200101 | 20210101): ").strip()
    filters['inventor'] = input("Inventor: ").strip()
    filters['country_code'] = input("Código do País (Ex: US, BR): ").strip()
    filters['assignee'] = input("Assignee (Empresa/Titular): ").strip()
    filters['ipc'] = input("Código IPC: ").strip()
    filters['publication_number'] = input("Número da Publicação: ").strip()
    filters['abstract_text'] = input("Termo para busca na Descrição: ").strip()
    filters['general_terms'] = input("Termo para busca geral (título, resumo, palavras-chave): ").strip()
            
    
    return {k: v for k, v in filters.items() if v}
