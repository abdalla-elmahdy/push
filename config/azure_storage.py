from decouple import config
from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    account_name = config("AZURE_ACCOUNT_NAME")
    account_key = config("AZURE_ACCOUNT_KEY")
    azure_container = "static"
    expiration_secs = None
