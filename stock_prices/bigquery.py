from google.cloud import bigquery
from google.oauth2 import service_account
from utils import get_client

# key_path = "msds_434.json"

# credentials = service_account.Credentials.from_service_account_file(key_path)
# project = 'msds-434-347202'
# client = bigquery.Client(project=project, credentials=credentials)


client = get_client()

query = """
    SELECT *
    FROM stock_prices.stock_details
"""

def query_bq():
    query_job = client.query(query) # make an API request
    df = query_job.to_dataframe()
    return df
    # print(df.head())

query_bq()
