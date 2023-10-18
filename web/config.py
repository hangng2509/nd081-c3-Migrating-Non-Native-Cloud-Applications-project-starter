import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdb-server-lab-3.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="admin123@techconfdb-server-lab-3" #TODO: Update value
    POSTGRES_PW="admin@Ne123"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://servicebus20231018.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Rb+OLRJvECcyJFB0mo7TxNI47RPq04xEw+ASbFRF/yI=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False