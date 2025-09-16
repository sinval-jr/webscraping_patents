import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response.text 

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    num_patent = soup.find(id = 'pubnum')
    title = soup.find('title').get_text()
    resume = soup.find(id = 'p-0001')
    print(f"Patent Number: {num_patent} \n Title: {title} \n Resume: {resume}")

    patent_citation_quantity = soup.find(id = 'patentCitations')
    print(f"Patent Citations: {patent_citation_quantity}")


if __name__ == "__main__":
    url = "https://patents.google.com/patent/CN113010302B/en?q=(computer+quantum)&oq=computer+quantum"
    page_content = fetch_page(url)
    parse_html(page_content)