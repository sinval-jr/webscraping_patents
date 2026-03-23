from google.oauth2 import service_account
from google.cloud import bigquery
import json

import dotenv
import os



dotenv.load_dotenv()

# Carrega as credenciais do serviço a partir da variável de ambiente
SERVICE_ACCOUNT_JSON_STR = json.loads(os.getenv("SERVICE_ACCOUNT_KEY"))

credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_JSON_STR,                                                                   scopes = ["https://www.googleapis.com/auth/cloud-platform"])
CLIENT = bigquery.Client(credentials=credentials, project=credentials.project_id)
