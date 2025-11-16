import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

query = '''
SELECT publication_number,`title_localized`[SAFE_OFFSET(0)].text
FROM `patents-public-data.patents.publications` 
WHERE
  REGEXP_CONTAINS(
    LOWER(`title_localized`[SAFE_OFFSET(0)].text),
    r'smart agriculture|smart farming|digital agriculture|digital farming|intelligent agriculture|intelligent farming|robotic farming|robotic agriculture|farming 4.0|agriculture 4.0|farming 5.0|agriculture 5.0|decision agriculture|decision farming|numerical agriculture|numerical farming|precision agriculture|precision farming|data-driven farming|data-driven agriculture|tech farming|tech agriculture|technological farming|technological agriculture|climatic-smart agriculture|climatic-smart farming|conservation agriculture|conservation farming|conservative agricutlure|conservative farming|sustainable agriculture|sustainable farming'
  ) or 
  REGEXP_CONTAINS(
    LOWER(`abstract_localized`[SAFE_OFFSET(0)].text),
    r'smart agriculture|smart farming|digital agriculture|digital farming|intelligent agriculture|intelligent farming|robotic farming|robotic agriculture|farming 4.0|agriculture 4.0|farming 5.0|agriculture 5.0|decision agriculture|decision farming|numerical agriculture|numerical farming|precision agriculture|precision farming|data-driven farming|data-driven agriculture|tech farming|tech agriculture|technological farming|technological agriculture|climatic-smart agriculture|climatic-smart farming|conservation agriculture|conservation farming|conservative agricutlure|conservative farming|sustainable agriculture|sustainable farming'
  )
'''

credentials = service_account.Credentials.from_service_account_file(filename ='GBQ.json', 
                                                                    scopes = ["https://www.googleapis.com/auth/cloud-platform"])

df = pd.read_gbq(query = query, credentials=credentials)
print(df.head())
df.to_csv('patents_data_regex.csv', index=False)
print("Data saved to patents_data.csv")