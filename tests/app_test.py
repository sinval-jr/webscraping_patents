import requests
import json
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response.content 

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    #num_patent = soup.find('dd', itemprop = 'assigneeOriginal').get_text()
    #title = soup.find('title').get_text()
    #resume = soup.find(id = 'p-0001').get_text()
    #print(f"Patent Number: {num_patent} \n Title: {title} \n Resume: {resume}")

    patent_citation_quantity = soup.findAll('table', )
    print(f"Patent Citations: {patent_citation_quantity}")


if __name__ == "__main__":
    publication_number = "US20240420214A1"
    url = "https://patents.google.com/patent" + "/" + publication_number + "/en"

    page_content = fetch_page(url)
    parse_html(page_content)