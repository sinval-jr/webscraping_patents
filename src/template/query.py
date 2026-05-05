
dict_campos_t1 ={
    "publication_number": "t1.publication_number AS publication_number",
    "application_number": "t1.application_number AS application_number",
    "country_code": "t1.country_code AS country_code",
    "kind_code":"t1.kind_code AS kind_code",
    "application_kind": "t1.application_kind AS application_kind",
    "application_number_formatted": "t1.application_number_formatted AS application_number_formatted",
    "pct_number": "t1.pct_number AS pct_number",
    "family_id": "t1.family_id AS family_id",
    "spif_publication_number": "t1.spif_publication_number as spif_publication_number",
    "spif_application_number": "t1.spif_application_number as spif_application_number",
    "publication_date": "t1.publication_date as publication_date",
    "filing_data": "t1.filing_data as filing_data",
    "grant_date": "t1.grant_date as grant_date",
    "priority_date": "t1.priority_date as priority_date",
    "inventor": "t1.inventor as inventor",
    "assignee": "t1.assignee as assignee",
    "entity_status": "t1.entity_status as entity_status",
    "art_unit": "t1.art_unit as art_unit"
}
dict_campos_title = {
    'title_text': 'title.text as title_text',
    'title_language': 'title.language as title_language',
    'title_truncated': 'title.truncated as title_truncated'
}
dict_campos_abstract = {
    'abstract_text': 'abstract.text as abstract_text',
    'abstract_language': 'abstract.language as abstract_language',
    'abstract_truncated': 'abstract.truncated as abstract_truncated'
}
dict_campos_claims = {
    'claims_text': 'claims.text as claims_text',
    'claims_language': 'claims.language as claims_language',
    'claims_truncated': 'claims.truncated as claims_truncated'
}

dict_campos_claims_html = {
    'claims_html_text': 'claims_html.text as claims_html_text',
    'claims_html_language': 'claims_html.language as claims_html_language',
    'claims_html_truncated': 'claims_html.truncated as claims_html_truncated'
}
#aqui
dict_campos_description = {
    'description_text': 'description.text as description_text',
    'description_language': 'description.language as description_language',
    'description_truncated': 'description.truncated as description_truncated'
}

dict_campos_description_html = {
    'description_html_text': 'description_html.text as description_html_text',
    'description_html_language': 'description_html.language as description_html_language',
    'description_html_truncated': 'description_html.truncated as description_html_truncated'
}

dict_campos_priority_claim ={
    'priority_publication_number': 'priority_claim.publication_number as priority_claim_publication_number',
    'priority_application_number': 'priority_claim.application_number as priority_claim_application_number',
    'priority_npl_text': 'priority_claim.npl_text as priority_claim_npl_text',
    'priority_type': 'priority_claim.type as priority_claim_type',
    'priority_category': 'priority_claim.category as priority_claim_category',
    'priority_filing_date': 'priority_claim.filing_date as priority_claim_filing_date'
}

dict_campos_inventor_harmonized = {
    'inventor_harmonized_name': 'inventor_harmonized.name as inventor_harmonized_name',
    'inventor_harmonized_country_code': 'inventor_harmonized.country_code as inventor_harmonized_country_code'
}

dict_campos_assignee_harmonized = {
    'assignee_harmonized_name': 'assignee_harmonized.name as assignee_harmonized_name',
    'assignee_harmonized_country_code': 'assignee_harmonized.country_code as assignee_harmonized_country_code'
}

dict_campos_examiner = {
    'examiner_name': 'examiner.name as examiner_name',
    'examiner_department': 'examiner.department as examiner_department',
    'examiner_level': 'examiner.level as examiner_level'    
}

dict_campos_uspc ={
    'uspc_code': 'uspc.code as uspc_code',
    'uspc_inventive': 'uspc.inventive as uspc_inventive',
    'uspc_first': 'uspc.first as uspc_first',
    'uspc_tree': 'uspc.tree as uspc_tree',
}
dict_campos_ipc = {
    'ipc_code': 'ipc.code as ipc_code',
    'ipc_inventive': 'ipc.inventive as ipc_inventive',
    'ipc_first': 'ipc.first as ipc_first',
    'ipc_tree': 'ipc.tree as ipc_tree',
}
dict_campos_ipcr = {
    'ipcr_code': 'ipcr.code as ipcr_code',
    'ipcr_inventive': 'ipcr.inventive as ipcr_inventive',
    'ipcr_first': 'ipcr.first as ipcr_first',
    'ipcr_tree': 'ipcr.tree as ipcr_tree',
}
dict_campos_fi = {
    'fi_code': 'fi.code as fi_code',
    'fi_inventive': 'fi.inventive as fi_inventive',
    'fi_first': 'fi.first as fi_first',
    'fi_tree': 'fi.tree as fi_tree',
}
dict_campos_fterm = {
    'ft_code': 'fterm.code as fterm_code',
    'ft_inventive': 'fterm.inventive as fterm_inventive',
    'ft_first': 'fterm.first as fterm_first',
    'ft_tree': 'fterm.tree as fterm_tree',
}
dict_campos_locarno = {
    'locarno_code': 'locarno.code as locarno_code',
    'locarno_inventive': 'locarno.inventive as locarno_inventive',
    'locarno_first': 'locarno.first as locarno_first',
    'locarno_tree': 'locarno.tree as locarno_tree',
}
dict_campos_citation = {
    'citation_publication_number': 'citation.publication_number as citation_publication_number',
    'citation_application_number': 'citation.application_number as citation_application_number',
    'citation_npl_text': 'citation.first as citation_first',
    'citation_type': 'citation.tree as citation_type',
    'citation_category': 'citation.tree as citation_category',
    'citation_filing_date': 'citation.filing_date as citation_filling_date'
}
dict_campos_parent = {
    'parent_publication_number': 'parent.publication_number as parent_publication_number',
    'parent_application_number': 'parent.application_number as parent_application_number',
    'parent_npl_text': 'parent.first as parent_first',
    'parent_type': 'parent.tree as parent_type',
    'parent_category': 'parent.tree as parent_category',
    'parent_filing_date': 'parent.filing_date as parent_filling_date'   
}
dict_campos_child = {
    'child_publication_number': 'child.publication_number as child_publication_number',
    'child_application_number': 'child.application_number as child_application_number',
    'child_npl_text': 'child.first as child_first',
    'child_type': 'child.tree as child_type',
    'child_category': 'child.tree as child_category',
    'child_filing_date': 'child.filing_date as child_filling_date'   
}

dict_from_bigquery = {
    't1': '`patents-public-data.patents.publications` AS t1',
    'title': 't1.title_localized AS title',
    'abstract': 't1.abstract_localized AS abstract',
    'claims': 't1.claims_localized AS claims',
    'claims_html': 't1.claims_localized_html AS claims_html',
    'description': 't1.description_localized AS description',
    'description_html': 't1.description_localized_html AS description_html',
    'priority_claim': 't1.priority_claim AS priority_claim',
    'inventor_harmonized': 't1.inventor_harmonized AS inventor_harmonized',
    'assignee_harmonized': 't1.assignee_harmonized AS assignee_harmonized',
    'examiner': 't1.examiner AS examiner',
    'uspc': 't1.uspc AS uspc',
    'ipc': 't1.ipc AS ipc',
    'ipcr': 't1.ipcr AS ipcr',
    'fi': 't1.fi AS fi',
    'fterm': 't1.fterm AS fterm',
    'locarno': 't1.locarno AS locarno',
    'citation': 't1.citation AS citation',
    'parent': 't1.parent AS parent',
    'child': 't1.child AS child',
}


mapeamento_fontes = {
    't1': dict_campos_t1,
    'title': dict_campos_title,
    'abstract': dict_campos_abstract,
    'claims': dict_campos_claims,
    'claims_html': dict_campos_claims_html,
    'description': dict_campos_description,
    'description_html': dict_campos_description_html,
    'priority_claim': dict_campos_priority_claim,
    'inventor_harmonized': dict_campos_inventor_harmonized,
    'assignee_harmonized': dict_campos_assignee_harmonized,
    'examiner': dict_campos_examiner,
    'uspc': dict_campos_uspc,
    'ipc': dict_campos_ipc,
    'ipcr': dict_campos_ipcr,
    'fi': dict_campos_fi,
    'fterm': dict_campos_fterm,
    'locarno': dict_campos_locarno,
    'citation': dict_campos_citation,
    'parent': dict_campos_parent,
    'child': dict_campos_child,
}

def gerar_query_patents(campos_desejados, limit=10000):
    # Agrupa todos os mapeamentos de campos
    todos_campos = {
        **dict_campos_t1, 
        **dict_campos_title,
        **dict_campos_abstract,
        **dict_campos_claims,
        **dict_campos_claims_html,
        **dict_campos_description,
        **dict_campos_description_html,
        **dict_campos_priority_claim,
        **dict_campos_inventor_harmonized,
        **dict_campos_assignee_harmonized,
        **dict_campos_examiner,
        **dict_campos_uspc,
        **dict_campos_ipc,
        **dict_campos_ipcr,
        **dict_campos_fi,
        **dict_campos_fterm,
        **dict_campos_locarno,
        **dict_campos_citation,
        **dict_campos_parent,
        **dict_campos_child,
    }
    
    # 1. Identifica as cláusulas SELECT
    select_clauses = [todos_campos[campo] for campo in campos_desejados if campo in todos_campos]
    
    # 2. Identifica quais fontes (FROM/UNNEST) são necessárias
    # Sempre incluímos a t1 (tabela principal)
    fontes_necessarias = ['t1']
    
    for campo in campos_desejados:
        if campo in dict_campos_title:
            fontes_necessarias.append('title')
        elif campo in dict_campos_abstract:
            fontes_necessarias.append('abstract')
        elif campo in dict_campos_claims:
            fontes_necessarias.append('claims')
        elif campo in dict_campos_claims_html:
            fontes_necessarias.append('claims_html')
        elif campo in dict_campos_description:
            fontes_necessarias.append('description')
        elif campo in dict_campos_description_html:
            fontes_necessarias.append('description_html')
        elif campo in dict_campos_priority_claim:
            fontes_necessarias.append('priority_claim')
        elif campo in dict_campos_inventor_harmonized:
            fontes_necessarias.append('inventor_harmonized')
        elif campo in dict_campos_assignee_harmonized:
            fontes_necessarias.append('assignee_harmonized')
        elif campo in dict_campos_examiner:
            fontes_necessarias.append('examiner')
        elif campo in dict_campos_uspc:
            fontes_necessarias.append('uspc')
        elif campo in dict_campos_ipc:
            fontes_necessarias.append('ipc')
        elif campo in dict_campos_ipcr:
            fontes_necessarias.append('ipcr')
        elif campo in dict_campos_fi:
            fontes_necessarias.append('fi')
        elif campo in dict_campos_fterm:
            fontes_necessarias.append('fterm')
        elif campo in dict_campos_locarno:
            fontes_necessarias.append('locarno')
        elif campo in dict_campos_citation:
            fontes_necessarias.append('citation')
        elif campo in dict_campos_parent:
            fontes_necessarias.append('parent')
        elif campo in dict_campos_child:
            fontes_necessarias.append('child')
            
    from_clauses = [dict_from_bigquery[fonte] for fonte in fontes_necessarias]

    # 3. Monta a String final
    query = "SELECT\n    "
    query += ",\n    ".join(select_clauses)
    query += "\nFROM\n    "
    query += ",\n    ".join(from_clauses)
    query += f"\nLIMIT {limit}"

    campos_por_fonte = {}
    for campo in campos_desejados:
        for fonte, mapeamento in mapeamento_fontes.items():
            if campo in mapeamento:
                if fonte not in campos_por_fonte:
                    campos_por_fonte[fonte] = []
                campos_por_fonte[fonte].append(campo)
                break
            
    print("Campos por fonte:", campos_por_fonte)
    return query,campos_por_fonte

# --- Exemplo de Uso ---

# Escolha as chaves que você quer extrair (conforme definido nos seus dicts)
def print_campos_disponiveis():
    print("Campos de tabela principal (t1):")
    for key in dict_campos_t1.keys():
        print(f"- {key}")
    print("Campos de tabela Title (title):")
    for key in dict_campos_title.keys():
        print(f"- {key}")
    print("Campos de tabela Abstract (abstract):")
    for key in dict_campos_abstract.keys():
        print(f"- {key}")
    print("Campos de tabela Claims (claims):")
    for key in dict_campos_claims.keys():
        print(f"- {key}")
    print("Campos de tabela Claims HTML (claims_html):")
    for key in dict_campos_claims_html.keys():
        print(f"- {key}")
    print("Campos de tabela Description (description):")
    for key in dict_campos_description.keys():
        print(f"- {key}")
    print("Campos de tabela Description HTML (description_html):")
    for key in dict_campos_description_html.keys():
        print(f"- {key}")
    print("Campos de tabela Priority Claim (priority_claim):")
    for key in dict_campos_priority_claim.keys():
        print(f"- {key}")
    print("Campos de tabela Inventor Harmonized (inventor_harmonized):")
    for key in dict_campos_inventor_harmonized.keys():
        print(f"- {key}")
    print("Campos de tabela Assignee Harmonized (assignee_harmonized):")
    for key in dict_campos_assignee_harmonized.keys():
        print(f"- {key}")
    print("Campos de tabela Examiner (examiner):")
    for key in dict_campos_examiner.keys():
        print(f"- {key}")
    print("Campos de tabela USPc (uspc):")
    for key in dict_campos_uspc.keys():
        print(f"- {key}")
    print("Campos de tabela IPC (ipc):")
    for key in dict_campos_ipc.keys():
        print(f"- {key}")
    print("Campos de tabela IPCR (ipcr):")
    for key in dict_campos_ipcr.keys():
        print(f"- {key}")
    print("Campos de tabela FI (fi):")
    for key in dict_campos_fi.keys():
        print(f"- {key}")
    print("Campos de tabela FTerm (fterm):")
    for key in dict_campos_fterm.keys():
        print(f"- {key}")
    print("Campos de tabela Locarno (locarno):")
    for key in dict_campos_locarno.keys():
        print(f"- {key}")
    print("Campos de tabela Citation (citation):")
    for key in dict_campos_citation.keys():
        print(f"- {key}")
    print("Campos de tabela Parent (parent):")
    for key in dict_campos_parent.keys():
        print(f"- {key}")
    print("Campos de tabela Child (child):")
    for key in dict_campos_child.keys():
        print(f"- {key}")

def print_limites_disponiveis():
    print("Limites disponíveis:")
    print("1. - 1000")
    print("2. - 5000")
    print("3. - 10000")
    