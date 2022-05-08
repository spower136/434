from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
import stock_prices
from utils import get_client
import pandas as pd
from os import path, environ

bigquery_client = get_client()

def bq_create_dataset():
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset('stock_prices')

    bigquery_client.get_dataset(dataset_ref)
    dataset = bigquery.Dataset(dataset_ref)
    dataset = bigquery_client.create_dataset(dataset)
    print('Dataset {} created.'.format(dataset.dataset_id))



def bq_create_table():
    # bigquery_client = bigquery.Client(project=project, credentials=credentials)
    dataset_ref = bigquery_client.dataset('stock_prices')

    # Prepares a reference to the table
    table_ref = dataset_ref.table('stock_details')
    table_ref = 'msds-434-347202.stock_prices.stock_details'

    # table = bigquery.Table('msds-434-347202.stock_prices.stock_details', schema=schema)
    table = bigquery_client.create_table(table)
    print('table {} created.'.format(table.table_id))



def main():
    root = path.dirname(path.abspath(__file__))
    df = stock_prices.get_df()
    df.to_csv('/tmp/stock_prices.csv',index=False)
    file_path = '/tmp/stock_prices.csv'
    data = path.join(root, file_path)

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
