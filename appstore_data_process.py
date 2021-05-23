import pandas as pd
from pandas.io.json import json_normalize

def appstore_processed_data(as_data):
    #as_df = pd.DataFrame(x['data'])
    as_df=json_normalize(as_data, record_path=['data'])
    as_df = as_df.rename({'id': 'ext_id'}, axis=1, inplace = False)
    as_df.drop(as_df.iloc[:, 6:40], inplace = True, axis = 1)
    as_df.to_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appstore_df.csv')
    return as_df
