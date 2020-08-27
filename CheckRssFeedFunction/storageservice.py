import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime

azure_storage_conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "rsshandler"
local_file_name = "checkpoint.txt"

def create_or_update_blob(now):
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    blob_client.upload_blob(str(now), overwrite=True)

def __get_checkpoint_blob__():
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    download_stream = blob_client.download_blob()
    checkpointbytes = download_stream.readall()
    return str(checkpointbytes, 'utf-8')

def get_checkpoint_datetime():
    checkpoint_datetime = datetime.utcnow
    checkpoint_datetime = datetime.strptime(__get_checkpoint_blob__(), '%Y-%m-%d %H:%M:%S.%f')
    return checkpoint_datetime