import os
import io
import pandas as pd
from authlib.jose import jwt

import sys
sys.path.append(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Config')
from af_as_config import secretkey, list_URL, key_id, issuer_id, path_to_key, appstore_url
from appfollow_api_integration import af_app_data_extraction 
from appfollow_data_process import af_data_process
from appstore_token_generation import get_token
from appstore_api_integration import app_store_data_extraction 
from appstore_data_process import appstore_processed_data

def combine():
    appstore=pd.read_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appstore_df.csv')
    appfollow=pd.read_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appfollow_df.csv')
    consolidated = pd.merge(appstore, appfollow, on='ext_id', how='left')
    test_sdk = consolidated['attributes.bundleId'].str.contains('test')
    consolidated=consolidated[~test_sdk]
    prototype_sdk = consolidated['attributes.bundleId'].str.contains('prototype')
    consolidated=consolidated[~prototype_sdk]
    status = []
    for row in consolidated['store']:
        if row=="itunes" :
            status.append('Integrated')
        else :
            status.append('Not Integrated')           
    # Creating a column named status
    consolidated['status'] = status
    consolidated.to_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/status_combine.csv')
    return consolidated

#api integration and data extraction of AppFollow, requires secret key and desired API URL
data=af_app_data_extraction(list_URL, secretkey)
af_data_process(data)
#af_data_process(af_app_data_extraction(list_URL, secretkey))

#api integration and data extraction of AppStore, requires JWT enrypted token, key_id, issuer_id and appstore API URL
token=get_token(path_to_key, key_id, issuer_id)
as_data=app_store_data_extraction(token, appstore_url )
appstore_processed_data(as_data)

#appstore_processed_data(app_store_data_extraction(get_token(path_to_key, key_id, issuer_id), appstore_url))


compare_data=combine()
print(compare_data)
