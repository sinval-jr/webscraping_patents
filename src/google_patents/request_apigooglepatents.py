import json
import requests


key_api = "ca95An2mdSGyhyM3inqbR2z4"
url = "https://www.searchapi.io/api/v1/search?api_key=" + key_api 
params = {
"engine": "google_patents",
"q": "ChatGPT",
"num": "100",
"patent_type": "patent"
}

response = requests.get(url, params=params)
json_arq = response.json()
object_json = json.dumps(json_arq, indent=4)
with open("google_patents_1.json","w") as file:
    file.write(object_json)
