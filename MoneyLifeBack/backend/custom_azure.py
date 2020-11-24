
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'moneylifestorage' # Must be replaced by your <storage_account_name>
    account_key = 'IewRModZCIHwQu24EAv1GsIQ0qsM+/3H2BTO82whJ17yS6A5TbctTaVyJuNkz/Kc8pscdbUE02CYp62OQDgHaw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'moneylifestorage' # Must be replaced by your storage_account_name
    account_key = 'JtEiG/BZUm3HSnPPXEpL9VaUX9z61MLjZAoiUiyjmL0Cb5Tn7vBre791m2G7adcsk07SReAIImofin+Q8haqdw==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None