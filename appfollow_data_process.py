

#function for appfollow data process
def af_data_process(data):
        import json
        import pandas as pd
        from pandas.io.json import json_normalize

        afjdata = json.loads(data)
        af_df = json_normalize(afjdata['apps_app'])
        #af_df=pd.DataFrame(afjdata[])
        af_df = af_df.drop(['app.lang', 'is_favorite','watch_url','count_whatsnew','has_reply_integration','app_id','app.url','app.kind','app.size', 'app.size','app.type'], axis=1)
        af_df_cleaned = af_df.rename({'app.ext_id':'ext_id'}, axis = 1)
        af_df_cleaned.to_csv('C:/Users/Sriram/Desktop/Data Team/Scripts/Data Quality/Output Files/appfollow_df.csv')
        return af_df_cleaned
