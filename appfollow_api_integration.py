import requests
from requests.auth import HTTPBasicAuth
import json
import sys
sys.path.append(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Config')
from af_as_config import secretkey, list_URL

def af_app_data_extraction(URL, key):
    response=requests.get(URL,auth=HTTPBasicAuth(key,''))
    return response.text

'''
def af_data_process(func):
        import json
        import pandas as pd
        from pandas.io.json import json_normalize

        afjdata = json.loads(func)
        af_df = json_normalize(afjdata['apps_app'])
        #af_df=pd.DataFrame(afjdata[])
        af_df = af_df.drop(['app.lang', 'is_favorite','watch_url','count_whatsnew','has_reply_integration','app_id','app.url','app.kind','app.size', 'app.size','app.type'], axis=1)
        af_df_cleaned = af_df.rename({'app.ext_id':'ext_id'}, axis = 1)
        af_df_cleaned.to_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appfollow_df.csv')
        return af_df_cleaned

#af_data_process(af_app_data_extraction(list_URL, secretkey))
'''
