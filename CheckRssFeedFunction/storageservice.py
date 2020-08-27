import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from datetime import datetime

azure_storage_conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "rsshandler"
local_file_name = "checkpoint.txt"
local_file_path = os.path.join("./", local_file_name)

def __write_todays_date__(now):
    local_path = "./"
    upload_file_path = os.path.join(local_path, local_file_name)

    file = open(upload_file_path, 'w')
    file.write(str(now))
    file.close()

    return upload_file_path

def create_or_update_blob(now):
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_conn_str)
    upload_file_path = __write_todays_date__(now)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

def __get_checkpoint_blob__():
    blob_service_client = BlobServiceClient.from_connection_string(azure_storage_conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    local_file_path = os.path.join("./", local_file_name)
    with open(local_file_path, "wb") as checkpoint:
        download_stream = blob_client.download_blob()
        checkpoint.write(download_stream.readall())

def get_checkpoint_datetime():
    __get_checkpoint_blob__()
    checkpoint_datetime = datetime.utcnow
    with open(local_file_path, "r") as checkpoint:
        checkpoint_str = checkpoint.read()
        checkpoint_datetime = datetime.strptime(checkpoint_str, '%Y-%m-%d %H:%M:%S.%f')
    return checkpoint_datetime