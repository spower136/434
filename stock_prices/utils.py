
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
import json


project = "msds-434-347202" 


def get_client(json_blob='msds_434.json'):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('msds_434')
    blob = bucket.blob(json_blob)
    print(blob)
    SERVICE_ACCOUNT_FILE = json.loads(blob.download_as_string(client=None))
    credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_FILE)
    client = bigquery.Client(project=project, credentials=credentials)

    return client

# get_client()


