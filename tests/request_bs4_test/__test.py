import requests
from bs4 import BeautifulSoup

class TestRequestBS4:
    def test_request_bs4(self):
        url = "https://www.google.com/patents/US20230214082A1"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to retrieve page, status code: {response.status_code}"
        
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()
        assert "US20230214082A1" in title, f"Title does not contain expected patent number, got: {title}"
        
        # Additional checks can be added here to verify specific content on the page
        print("Request and parsing successful, title:", title)

