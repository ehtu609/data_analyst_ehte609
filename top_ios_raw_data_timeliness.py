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

def top_funnel_ios_report():
    rx = '(top_funnel_ios_.*.csv$)'
    for (root,dirs,files) in os.walk(r'C:\Users\Sriram\Desktop\Data Team\Data\Raw Data\Top Funnel\IOS', topdown=True):
        for file in files:
            res = re.match(rx, file)
            if res:
                if res.group(1):
                    substring=file[-14:-4]
                    dated_substring=datetime.strptime(substring, '%Y-%m-%d')
                    dated_substring=dated_substring.date()
                    #print(dated_substring)
                    #print(file)
                else:
                    continue
            else:
                continue

    
    #function to generate verification column status showing if its the latest reports as per the condition
    #Walking through the directory to find files in every folder
    #for (root,dirs,files) in os.walk(r'C:\Users\Sriram\Desktop\Data Team\Data\Raw Data\Top Funnel\IOS\reports', topdown=True):
        #for file in files:
            #taking substring of the file name which contains the date in string format
            #substring=file[-14:-4]
            #Converting that string format date into datetime(needed for applying condition)
            #dated_substring=datetime.strptime(substring, '%Y-%m-%d')
            #this results in only date excluding time, hour, min and sec
            #dated_substring=dated_substring.date()
            #file_date.append(dated_substring)
            #print(dated_substring)

            #datetime module contains a function to get the current date
            current_date=datetime.today()
            #to get only the date excluding the time, hours, min, and sec
            current_date=current_date.date()
            #print(current_date)

            #applying the mathematical expression to further use the value in condtion according the report generation time
            difference_in_dates=current_date - dated_substring
            #this makes the resultant difference in dates into numeric values of 1 day rather than 1 day and included time
            difference_in_days=difference_in_dates.days
            #print(difference_in_days)
            #datetime.timedelta(days=1)):
            #diff_days=timedelta(days=1)

            #making empty list to later convert into seperate columns for the report
            critical_view=[]
            critical_view_ID=[]
            reports_name=[]
            fetch_file_until_date=[]
            curr_date_list=[]

            #so like the latest dates for the reports extraction is a day behind in ios raw top funnel data
            if (difference_in_days==1):
                critical_view_ID.append("CVBR1")
                reports_name.append("appfollow ios top funnel")
                critical_view.append("Updated")
                fetch_file_until_date.append(dated_substring)
                curr_date_list.append(current_date)
                
                timeliness_reports={'Business Rule no.':critical_view_ID,'Reports name':reports_name,'Status':critical_view, 'Reports Date':fetch_file_until_date, 'Current Date':curr_date_list}
                
                df=DataFrame(timeliness_reports, columns=['Business Rule no.', 'Reports name','Status', 'Reports Date', 'Current Date'])
                
            else:
                critical_view_ID.append("CVBR1")
                reports_name.append("appfollow ios top funnel")
                critical_view.append("Not Updated")
                fetch_file_until_date.append(dated_substring)
                curr_date_list.append(current_date)
                timeliness_reports={'Business Rule no.':critical_view_ID,'Reports name':reports_name,'Status':critical_view, 'Reports Date':fetch_file_until_date, 'Current Date':curr_date_list}
                df=DataFrame(timeliness_reports, columns=['Business Rule no.','Reports name', 'Status', 'Reports Date', 'Current Date'])
        #saving the created dataframe into a scv report and keeping index false to have no extra side columns
    df.to_csv(r'C:\Users\Sriram\Desktop\Data Team\Scripts\Data Quality\Output Files\redflag_reports.csv', index=False)
top_funnel_ios_report()
