from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
import stock_prices
from utils import get_client
import pandas as pd
from os import path, environ
import tempfile

bigquery_client = get_client()

def bq_create_dataset():
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('stock_prices')

    bigquery_client.get_dataset(dataset_ref)
    dataset = bigquery.Dataset(dataset_ref)
    dataset = bigquery_client.create_dataset(dataset)
    print('Dataset {} created.'.format(dataset.dataset_id))



def bq_create_table():
    bigquery_client = bigquery.Client(project=project, credentials=credentials)
    dataset_ref = bigquery_client.dataset('stock_prices')

    # Prepares a reference to the table
    table_ref = dataset_ref.table('stock_details')
    table_ref = 'msds-434-347202.stock_prices.stock_details'

    table = bigquery.Table('msds-434-347202.stock_prices.stock_details', schema=schema)
    table = bigquery_client.create_table(table)
    print('table {} created.'.format(table.table_id))

# def upload_blob():
#     """Uploads a file to the bucket."""
#     # The ID of your GCS bucket
    
#     bucket_name = "msds_434"
#     # The path to your file to upload
#     source_file_name = "stock_prices.csv"
#     # The ID of your GCS object
#     destination_blob_name = "stock_prices"

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)

#     print(
#         "File {} uploaded to {}.".format(
#             source_file_name, destination_blob_name
#         )
#     )

# def get_csv(filename='stock_prices'):
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket('msds_434')
#     # blob = bucket.blob(filename)
#     # print(blob)
#     # SERVICE_ACCOUNT_FILE = json.loads(blob.download_as_string(client=None))
#     # credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_FILE)
#     # client = bigquery.Client(project=project, credentials=credentials)
#     temp = pd.read_csv('gs://' + 'msds_434' + '/' + filename, sep=',')
#     return temp

# def get_file_path(file_name):
#     # file_name = secure_filename(filename)
#     return os.path.join(tempfile.gettempdir(), file_name)

# def write_temp_dir(data):
#     # data = [['tom', 10], ['nick', 15]] 
#     df = pd.DataFrame(data)
#     name = 'stock_prices.csv'
#     path_name = get_file_path(name)
#     print(path_name)
#     data = df.to_csv(path_name, index=False)
#     print(data)
#     return data

    # os.remove(path_name)


def main():
    root = path.dirname(path.abspath(__file__))
    df = stock_prices.get_df()
    # temp = write_temp_dir(df)
    # print(temp)
    df.to_csv('/tmp/stock_prices.csv',index=False)
    file_path = '/tmp/stock_prices.csv'
    data = path.join(root, file_path)
    # print(file_path)
    # store_data = upload_blob()
    # data = get_csv()
    
    # Instantiates a client
    # bigquery_client = bigquery.Client(project=project, credentials=credentials)

    # Prepares a reference to the dataset
    dataset_ref = bigquery_client.dataset('stock_prices')

    table_ref = dataset_ref.table('stock_details')
    table = bigquery_client.get_table(table_ref)  # API call

    job_config = bigquery.LoadJobConfig(
        schema = [
            bigquery.SchemaField('Date', 'STRING', mode='NULLABLE'),
            bigquery.SchemaField('Open', 'FLOAT', mode='NULLABLE'),
            bigquery.SchemaField('HIGH', 'FLOAT', mode='NULLABLE'),
            bigquery.SchemaField('Low', 'FLOAT', mode='NULLABLE'),
            bigquery.SchemaField('Close', 'FLOAT', mode='NULLABLE'),
            bigquery.SchemaField('Volume', 'NUMERIC', mode='NULLABLE'),
            bigquery.SchemaField('Dividends', 'NUMERIC', mode='NULLABLE'),
            bigquery.SchemaField('Stock_Splits', 'BOOLEAN', mode='NULLABLE'),
            bigquery.SchemaField('Symbol', 'STRING', mode='NULLABLE'),
        ],

        write_disposition="WRITE_APPEND",
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
        field_delimiter = ','
    )


    job = bigquery_client.load_table_from_file(
        open(data, "rb"), table , job_config=job_config
    )  # Make an API request.
    job.result()  # Wait for the job to complete.


main()
