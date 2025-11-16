import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import quote_plus

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

def fetch_page(url: str):
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar a URL: {e}")
        return None1

def parse_patent_data(html: bytes) -> dict:
    if not html:
        return {}
        
    soup = BeautifulSoup(html, 'html.parser')
    patent_data = {}
    
    def get_element_text(parent, tag, attrs={}):
        element = parent.find(tag, attrs)
        return element.get_text(strip=True) if element else None

    patent_data['title'] = get_element_text(soup, 'span', {'itemprop': 'title'})
    patent_data['publication_number'] = get_element_text(soup, 'dd', {'itemprop': 'publicationNumber'})
    patent_data['assignee_original'] = get_element_text(soup, 'dd', {'itemprop': 'assigneeOriginal'})
    patent_data['assignee_current'] = get_element_text(soup, 'dd', {'itemprop': 'assigneeCurrent'})
    patent_data['country_name'] = get_element_text(soup, 'dd', {'itemprop': 'countryName'})
    patent_data['priority_date'] = get_element_text(soup, 'dd', {'itemprop': 'priorityDate'})
    patent_data['publication_date'] = get_element_text(soup, 'dd', {'itemprop': 'publicationDate'})
    patent_data['abstract'] = get_element_text(soup, 'div', {'id': 'p-0001'})
    
    patent_data['citations'] = []
    citation_header = soup.find("h2", string=lambda text: text and "Patent Citation" in text)
    if citation_header:
        citation_table = citation_header.find_next("table")
        if citation_table:
            for row in citation_table.find_all("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    citation = {
                        "publication_number": get_element_text(cols[0], 'a'),
                        "priority_date": cols[1].get_text(strip=True),
                        "publication_date": cols[2].get_text(strip=True),
                        "assignee": cols[3].get_text(strip=True),
                        "title": cols[4].get_text(strip=True),
                    }
                    patent_data['citations'].append(citation)
    return patent_data

def search_and_get_patent_links(query: str, max_links: int) -> list:
    formatted_query = quote_plus(query)
    search_url = f"https://patents.google.com/?q=({formatted_query})"
    
    print(f"Buscando a página de resultados para: '{query}'")
    html = fetch_page(search_url)
    
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    
    links = []
    results = soup.select("article.search-result h2 a[href^='/patent/']")
    
    for link in results:
        full_url = "https://patents.google.com" + link['href']
        links.append(full_url)
        if len(links) >= max_links:
            break
            
    return links

if __name__ == "__main__":
    # --- EDITE AS VARIÁVEIS AQUI ---
    SEARCH_QUERY = "computer science"
    LIMIT = 5
    # ---------------------------------
    
    patent_urls = search_and_get_patent_links(SEARCH_QUERY, max_links=LIMIT)

    if not patent_urls:
        print("Nenhum link de patente encontrado. Encerrando.")
    else:
        print(f"\nEncontrados {len(patent_urls)} links. Iniciando extração de dados...")
        
        all_patents_data = []
        
        for i, url in enumerate(patent_urls):
            print(f"Extraindo dados de [{i+1}/{len(patent_urls)}]: {url}")
            
            page_content = fetch_page(url)
            if page_content:
                data = parse_patent_data(page_content)
                data['url'] = url
                all_patents_data.append(data)
            
            time.sleep(1)

        if all_patents_data:
            filename = f"patents_{SEARCH_QUERY.replace(' ', '_')}.json"
            print(f"\n✅ Extração concluída. Salvando dados em '{filename}'...")
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(all_patents_data, f, indent=4, ensure_ascii=False)
            
            print(f"✅ Dados salvos com sucesso em '{filename}'")