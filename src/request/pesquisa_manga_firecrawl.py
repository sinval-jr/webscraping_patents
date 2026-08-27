import os
import requests
import json

API_KEY = os.environ.get("FIRECRAWL_API_KEY", "fc-9c599a861b2144549c6b986beee86613")

def pesquisar_preco_manga():
    print("Iniciando pesquisa de mercado para 'manga'...")
    search_url = "https://api.firecrawl.dev/v1/search"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    search_payload = {
        "query": "cotação preço manga kg mercado brasil",
        "limit": 2
    }
    
    print("Buscando URLs relevantes...")
    response = requests.post(search_url, headers=headers, json=search_payload)
    
    if response.status_code != 200:
        print(f"Erro na pesquisa: {response.text}")
        return
        
    results = response.json().get("data", [])
    urls = [res["url"] for res in results]
    
    if not urls:
        print("Nenhuma URL encontrada na pesquisa.")
        return
        
    print(f"Fontes encontradas: {urls}")
    
    print("Extraindo os valores estratégicos das páginas...")
    
    for url in urls:
        scrape_url = "https://api.firecrawl.dev/v1/scrape"
        scrape_payload = {
            "url": url,
            "formats": ["extract"],
            "extract": {
                "prompt": "Extraia o preço da manga (mango) no mercado/cotação. Queremos o valor numérico e a unidade (ex: kg ou caixa).",
                "schema": {
                    "type": "object",
                    "properties": {
                        "produto": {"type": "string"},
                        "preco_reais": {"type": "number"},
                        "unidade": {"type": "string"},
                        "local_ou_fonte": {"type": "string"}
                    },
                    "required": ["produto", "preco_reais", "unidade"]
                }
            }
        }
        
        extract_resp = requests.post(scrape_url, headers=headers, json=scrape_payload)
        
        if extract_resp.status_code == 200:
            data = extract_resp.json()
            extracted_data = data.get("data", {}).get("extract", {})
            print(f"\nResultado da extração de ({url}):")
            print(json.dumps(extracted_data, indent=4, ensure_ascii=False))
        else:
            print(f"Erro ao extrair da URL {url}: {extract_resp.text}")

if __name__ == "__main__":
    pesquisar_preco_manga()
