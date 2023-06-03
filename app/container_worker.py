# https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python
# pip install azure-identity

from typing import Any
from azure.identity import DefaultAzureCredential
# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli
# pip install azure-storage-blob azure-identity

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json

class ContainerWorker():
    def __init__(self):
        self.config = self.read_config()
        self.account = self.config["storageaccountname"]

    def read_config(self):
        try:
            with open("app\config.json", "r") as jsonfile:
                data_config = json.load(jsonfile)
                print(data_config)
        except Exception as ex:
            print(ex)
        return data_config

    def get_container(self):
        data_dict = {"name": self.account}
        self.account_url = "https://" + self.account +".blob.core.windows.net"
        self.default_credential = DefaultAzureCredential()
        data = []
        try:
            blob_service_client = BlobServiceClient(account_url=self.account_url, credential=self.default_credential)
            blob_list =  blob_service_client.list_containers()
            for b in blob_list:
                print(b.name)
                data.append(b.name)
        except Exception as ex:
            print(ex)
        data_dict["values"] = data
        return data_dict

