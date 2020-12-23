from bs4 import BeautifulSoup
import csv
import requests
import time
import pandas as pd
import urllib
import re
import pickle
from lxml import html
import numpy as np

headers =   ['Index','Average temperature (°F)', 'Average humidity (%)',
 'Average dewpoint (°F)', 'Average barometer (in)',
 'Average windspeed (mph)', 'Average gustspeed (mph)',
 'Average direction (°deg)', 'Rainfall for month (in)',
 'Rainfall for year (in)', 'Maximum rain per minute',
 'Maximum temperature (°F)', 'Minimum temperature (°F)',
 'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
 'Minimum pressure', 'Maximum windspeed (mph)',
 'Maximum gust speed (mph)', 'Maximum heat index (°F)']

data = pd.DataFrame(columns = headers)

def fill_data_Index(url,l,year,month):
    r = requests.get(url)
    tree = html.fromstring(r.content)
    days = tree.xpath("//td[contains(., 'Average and Extremes') and not(contains(.,'for Month of'))]/text()")
    type(days)
    for i in range (len(days)):
        res = [int(j) for j in days[i].split() if j.isdigit()]
        days[i] = str(year)+'-'+str(month)+'-'+str(res[0])
    l.append(days)


def fill_data_Other_Attrbutes(url, xpath_param, col_param, lo):
    r = requests.get(url)
    tree = html.fromstring(r.content)
    at = tree.xpath("//td[contains(., 'Average and Extremes') and not(contains(.,'for Month of'))]//parent::tr//following-sibling::tr//td[.='"+xpath_param+"']//following-sibling::td//text()")
    type(at)
    lo.append(at)

year_diff= (2018-2009+1)
li_index=[]
li_1,li_2,li_3,li_4,li_5,li_6,li_7,li_8,li_9,li_10,li_11,li_12,li_13,li_14,li_15,li_16,li_17,li_18,li_19=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for i in range(year_diff):
    year = 2009+i
    for i in range (12):
        if(i<=8):
           yearmmonth = 'http://www.estesparkweather.net/archive_reports.php?date='+str(year)+str(0)+str(i+1)
           fill_data_Index(yearmmonth,li_index,year,str(0)+str(i+1))

        else:
           yearmmonth = 'http://www.estesparkweather.net/archive_reports.php?date='+str(year)+str(i+1)
           fill_data_Index(yearmmonth,li_index,year,str(i+1))

        fill_data_Other_Attrbutes(yearmmonth,'Average temperature', 'Average temperature (°F)',li_1)
        fill_data_Other_Attrbutes(yearmmonth,'Average humidity', 'Average humidity (%)',li_2)
        fill_data_Other_Attrbutes(yearmmonth,'Average dewpoint', 'Average dewpoint (°F)',li_3)
        fill_data_Other_Attrbutes(yearmmonth,'Average barometer', 'Average barometer (in)',li_4)
        fill_data_Other_Attrbutes(yearmmonth,'Average windspeed', 'Average windspeed (mph)',li_5)
        fill_data_Other_Attrbutes(yearmmonth,'Average gustspeed', 'Average gustspeed (mph)',li_6)
        fill_data_Other_Attrbutes(yearmmonth,'Average direction', 'Average direction (°deg)',li_7)
        fill_data_Other_Attrbutes(yearmmonth,'Rainfall for month', 'Rainfall for month (in)',li_8)
        fill_data_Other_Attrbutes(yearmmonth,'Rainfall for year',  'Rainfall for year (in)',li_9)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum rain per minute',  'Maximum rain per minute',li_10)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum temperature',  'Maximum temperature (°F)',li_11)
        fill_data_Other_Attrbutes(yearmmonth,'Minimum temperature',  'Minimum temperature (°F)',li_12)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum humidity',  'Maximum humidity (%)',li_13)
        fill_data_Other_Attrbutes(yearmmonth,'Minimum humidity',  'Minimum humidity (%)',li_14)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum pressure',  'Maximum pressure',li_15)
        fill_data_Other_Attrbutes(yearmmonth,'Minimum pressure',  'Minimum pressure',li_16)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum windspeed',  'Maximum windspeed (mph)',li_17)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum gust speed',  'Maximum gust speed (mph)',li_18)
        fill_data_Other_Attrbutes(yearmmonth,'Maximum heat index',  'Maximum heat index (°F)',li_19)

        print(yearmmonth)

        if(year == 2018 and i==10):
            break


    if(year == 2018   ):
         break
def add_to_frame(li, col_par):
    buff = []
    row = len(li)
    for i in range(row):
      col = len(li[i])
      for j in range (col):
         buff.append(li[i][j])
    data[col_par] = buff

add_to_frame(li_index, 'Index')
add_to_frame(li_1, 'Average temperature (°F)')
add_to_frame(li_2, 'Average humidity (%)')
add_to_frame(li_3, 'Average dewpoint (°F)')
add_to_frame(li_4, 'Average barometer (in)')
add_to_frame(li_5, 'Average windspeed (mph)')
add_to_frame(li_6, 'Average gustspeed (mph)')
add_to_frame(li_7, 'Average direction (°deg)')
add_to_frame(li_8, 'Rainfall for month (in)')
add_to_frame(li_9, 'Rainfall for year (in)')
add_to_frame(li_10,'Maximum rain per minute')
add_to_frame(li_11,'Maximum temperature (°F)')
add_to_frame(li_12,'Minimum temperature (°F)')
add_to_frame(li_13,'Maximum humidity (%)')
add_to_frame(li_14,'Minimum humidity (%)')
add_to_frame(li_15,'Maximum pressure')
add_to_frame(li_16,'Minimum pressure')
add_to_frame(li_17,'Maximum windspeed (mph)')
add_to_frame(li_18,'Maximum gust speed (mph)')
add_to_frame(li_19,'Maximum heat index (°F)')

indexedData = data.set_index('Index')
indexedData.drop(indexedData.tail(27).index,inplace=True) # drop last n rows
indexedData.index = pd.to_datetime(indexedData.index, format='%Y-%m-%d')
indexedData.info()
indexedData.head()

# cleaning operations
indexedData['Average temperature (°F)'] = indexedData['Average temperature (°F)'].apply(lambda x: x.replace('°F', '').strip()).astype('float')
indexedData['Average humidity (%)'] = indexedData['Average humidity (%)'].apply(lambda x: x.replace('%', '').strip()).astype('float')
indexedData['Average dewpoint (°F)'] = indexedData['Average dewpoint (°F)'].apply(lambda x: x.replace('°F', '').strip()).astype('float')
indexedData['Average barometer (in)'] = indexedData['Average barometer (in)'].apply(lambda x: x.replace('in.', '').strip()).astype('float')
indexedData['Average windspeed (mph)'] = indexedData['Average windspeed (mph)'].apply(lambda x: x.replace('mph', '').strip()).astype('float')
indexedData['Average gustspeed (mph)'] = indexedData['Average gustspeed (mph)'].apply(lambda x: x.replace('mph', '').strip()).astype('float')
indexedData['Average direction (°deg)'] = indexedData['Average direction (°deg)'].apply(lambda x: x.split('°')[0]).astype('float')
indexedData['Rainfall for month (in)'] = indexedData['Rainfall for month (in)'].apply(lambda x: x.replace('in.', '').strip()).astype('float')
indexedData['Rainfall for year (in)'] = indexedData['Rainfall for year (in)'].apply(lambda x: x.replace('in.', '').strip()).astype('float')
indexedData['Maximum rain per minute'] = indexedData['Maximum rain per minute'].apply(lambda x: x.split('in')[0].strip()).astype('float')
indexedData['Maximum temperature (°F)'] = indexedData['Maximum temperature (°F)'].apply(lambda x: x.split('°F')[0].strip()).astype('float')
indexedData['Minimum temperature (°F)'] = indexedData['Minimum temperature (°F)'].apply(lambda x: x.split('°F')[0].strip()).astype('float')
indexedData['Maximum humidity (%)'] = indexedData['Maximum humidity (%)'].apply(lambda x: x.split('%')[0].strip()).astype('float')
indexedData['Minimum humidity (%)'] = indexedData['Minimum humidity (%)'].apply(lambda x: x.split('%')[0].strip()).astype('float')
indexedData[ 'Maximum pressure'] = indexedData[ 'Maximum pressure'].apply(lambda x: x.split('in')[0].strip()).astype('float')
indexedData[ 'Minimum pressure'] = indexedData[ 'Minimum pressure'].apply(lambda x: x.split('in')[0].strip()).astype('float')
indexedData[ 'Maximum windspeed (mph)'] = indexedData[ 'Maximum windspeed (mph)'].apply(lambda x: x.split('mph')[0].strip()).astype('float')
indexedData[ 'Maximum gust speed (mph)'] = indexedData[ 'Maximum gust speed (mph)'].apply(lambda x: x.split('mph')[0].strip()).astype('float')
indexedData['Maximum heat index (°F)'] = indexedData['Maximum heat index (°F)'].apply(lambda x: x.split('°F')[0].strip()).astype('float')

# Writing to pickle file
with open('question/dataframe.pk', "wb") as file:
    pickle.dump(indexedData, file)




