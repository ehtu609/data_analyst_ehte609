#using operating system libararies to use the walk function which will help in waling through directories files
import os
import re
#will be needed for creating dataframes and even reading the csv files as dataframe
import pandas as pd
#we import the function DataFrame to improve code readability
from pandas import DataFrame
#python has special datetime module which helps in finding the current date and converting strings to datetime
#timedelta is special keyword which has its special of going back in date or front in date
from datetime import datetime, timedelta

def ios_subscription_report():
    rx = '(Subscription_Event_85875515_.*V1_2.txt$)'
    for (root,dirs,files) in os.walk(r'C:\Users\Sriram\Desktop\KPI Dashboard\Reporter\Subscriber Reports', topdown=True):
        for file in files:
            res = re.match(rx, file)
            if res:
                if res.group(1):
                    substring=file[-17:-9]
                    dated_substring=datetime.strptime(substring, '%Y%m%d')
                    dated_substring=dated_substring.date()
                    #print(dated_substring)
                    #print(file)
                else:
                    continue
            else:
                continue
    
    #function to generate verification column status showing if its the latest reports or not
    #walking through the directory for files
    #for (root,dirs,files) in os.walk(r'C:\Users\Sriram\Desktop\KPI Dashboard\Reporter\Subcriber Reports_V1_2', topdown=True):
        #for file in files:
            #for the current naming system 'Subscription_Event_85875515_20201110_V1_2' the below code will get substring containing date string
            #substring=file[-17:-9]
            #print(substring)"""
            #important to remember the format 'Y' works for four digit year and m works months ignoring 0
            #the fomrat maydiffer according the date string in the filename
            #dated_substring=datetime.strptime(substring, '%Y%m%d')
            #dated_substring=dated_substring.date()

            current_date=datetime.today()
            current_date=current_date.date()
            #print(dated_substring)
            
            difference_in_dates=current_date - dated_substring
            difference_in_days=difference_in_dates.days

            #reading the same report csv file created to either append a new fresh row or update the existing
            df=pd.read_csv(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Data Quality\Output Files\redflag_reports.csv')

           #here we are checking if the row is present or not, if not we append to make a new row
            if "CVBR2" in df["Business Rule no."].unique():
                pass
                            
            else:
                 df=df.append({'Business Rule no.':"CVBR2", 'Reports name': "ios subscription", 'Status':"Updated",'Reports Date':dated_substring,'Current Date':current_date}, ignore_index=True)

            #important condition check is done here and the coulmn status is updated or not updated           
            if (difference_in_days<=2):
                df.loc[df['Business Rule no.'] == "CVBR2", 'Status'] = "Updated"
                df.loc[df['Business Rule no.'] == "CVBR2", 'Reports Date'] = dated_substring 
                df.loc[df['Business Rule no.'] == "CVBR2", 'Current Date'] = current_date
            else:
                df.loc[df['Business Rule no.'] == "CVBR2", 'Status'] = "Not Updated"
                df.loc[df['Business Rule no.'] == "CVBR2", 'Reports Date'] = dated_substring 
                df.loc[df['Business Rule no.'] == "CVBR2", 'Current Date'] = current_date

    #saving the dataframe into the same reports csv filefor further continous visualisation            
    df.to_csv(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Data Quality\Output Files\redflag_reports.csv', index=False)

ios_subscription_report()
