import sys
sys.path.append(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Config')

from af_as_config import appstore_url, path_to_key, key_id, issuer_id
import requests, time, json 
from authlib.jose import jwt
from pandas.io.json import json_normalize

def get_token(path_to_key, key_id, issuer_id):
    KEY_ID = key_id
    ISSUER_ID = issuer_id
    EXPIRATION_TIME = int(round(time.time()))
    with open(path_to_key, 'r') as f:
        PRIVATE_KEY = f.read()
        header = {
        "alg": "ES256",
        "kid": KEY_ID,
        "typ": "JWT"
        }

        payload = {
        "iss": ISSUER_ID,
        "exp": EXPIRATION_TIME,
        "aud": "appstoreconnect-v1"
        }
        return jwt.encode(header, payload, PRIVATE_KEY)



def app_store_data_extraction(func, appstore_url):
    JWT = 'Bearer ' + func.decode()
    URL = appstore_url
    HEAD = {'Authorization': JWT}

    r = requests.get(URL, params={'limit': 200}, headers=HEAD)

    return r.json()
'''
def appstore_processed_data(func):
    #as_df = pd.DataFrame(x['data'])
    as_df=json_normalize(func, record_path=['data'])
    as_df = as_df.rename({'id': 'ext_id'}, axis=1, inplace = False)
    as_df.drop(as_df.iloc[:, 6:40], inplace = True, axis = 1)
    as_df.to_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appstore_df.csv')
    return as_df

#as_data=app_store_data_extraction(get_token(path_to_key, key_id, issuer_id), appstore_url)
appstore_processed_data(app_store_data_extraction(get_token(path_to_key, key_id, issuer_id), appstore_url))
'''
