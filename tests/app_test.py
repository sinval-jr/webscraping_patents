import requests
from bs4 import BeautifulSoup
import json

# Configuração da sessão HTTP
session = requests.Session()

# Definindo um User-Agent para evitar bloqueios por parte do servidor
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

def fetch_page(url: str):
    """
    Busca o conteúdo HTML de uma página (faz a requisição).
    """
    try:
        response = session.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar a URL: {e}")
        return None

def parse_patent_data(html: bytes) -> dict:
    """
    Extrai dados relevantes da página HTML da patente e transforma eles em json.
    """
    if not html:
        return {}
        
    soup = BeautifulSoup(html, 'html.parser')
    patent_data = {}

    # Função auxiliar para evitar repetição e tratar erros
    def get_element_text(parent, tag, attrs={}):
        element = parent.find(tag, attrs)
        return element.get_text(strip=True) if element else None

    # Extração de dados com verificação de existência
    patent_data['title'] = get_element_text(soup, 'span', {'itemprop': 'title'})
    patent_data['publication_number'] = get_element_text(soup, 'dd', {'itemprop': 'publicationNumber'})
    patent_data['assignee_original'] = get_element_text(soup, 'dd', {'itemprop': 'assigneeOriginal'})
    patent_data['assignee_current'] = get_element_text(soup, 'dd', {'itemprop': 'assigneeCurrent'})
    patent_data['country_name'] = get_element_text(soup, 'dd', {'itemprop': 'countryName'})
    #patent_data['priority_date'] = get_element_text(soup, 'dd', {'itemprop': 'priorityDate'})
    #patent_data['publication_date'] = get_element_text(soup, 'dd', {'itemprop': 'publicationDate'})
    patent_data['abstract'] = get_element_text(soup, 'div', {'num': '0001'})
    
    # Extração das citações (exemplo mais complexo)
    patent_data['citations'] = []
    citation_header = soup.find("h2", string=lambda text: text and "Patent Citation" in text)
    if citation_header:
        citation_table = citation_header.find_next("table")
        if citation_table:
            # Itera sobre as linhas da tabela, pulando o cabeçalho
            for row in citation_table.find_all("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) >= 5: # Garante que a linha tem colunas suficientes
                    citation = {
                        "publication_number": get_element_text(cols[0], 'a'),
                        "priority_date": cols[1].get_text(strip=True),
                        "publication_date": cols[2].get_text(strip=True),
                        "assignee": cols[3].get_text(strip=True),
                        "title": cols[4].get_text(strip=True),
                    }
                    patent_data['citations'].append(citation)

    return patent_data

if __name__ == "__main__":
    publication_number = "CN111909735A" 
    filename = f"{publication_number}.json"
    url = f"https://patents.google.com/patent/{publication_number}/en"

    print(f"Buscando dados da patente: {publication_number}...")
    page_content = fetch_page(url)
    
    
    if page_content:
        data = parse_patent_data(page_content)
        print("\n--- Dados da Patente ---")
        print(json.dumps(data, indent=4, ensure_ascii=False))
        

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"\n✅ Dados salvos com sucesso em '{filename}'")