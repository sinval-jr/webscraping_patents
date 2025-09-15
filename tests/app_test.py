import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response.text 

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    num_patent = soup.find(id = 'pubnum', class_ = 'style-scope patent-result')
    title = soup.find('title').get_text()
    print(f"Patent Number: {num_patent} \n Title: {title}")


if __name__ == "__main__":
    url = "https://patents.google.com/patent/US12367394B2/en?oq=US12367394B2"
    page_content = fetch_page(url)
    parse_html(page_content)