#Import necessary modules

import glob
import urllib.request
from datetime import datetime
import pandas as pd
import requests
import bs4
import zipfile

def extract_from_csv(file_to_process):
    #encoding added to avoid decoding errors
    dataframe=pd.read_csv(file_to_process,encoding='ISO-8859-1')
    return dataframe

def extract_from_excel(file_to_process):
    dataframe=pd.read_excel(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe=pd.read_json(file_to_process)
    return dataframe

def extract_from_files():
    #dowloading the zip file from github
    urllib.request.urlretrieve('https://github.com/barnitarc/Data-Engineering-Project-1/raw/main/Source%20Files/Source%20Files.zip',filename='SourceFiles.zip')
    
    #unzipping the files
    with zipfile.ZipFile('SourceFiles.zip') as f:
        f.extractall('d:/Python for Data Engineering Project/Project1/')
    
    #creating DataFrame for each files
        
    '''CSV files
        1. countries-continents-capitals.csv
        2. world-population-by-country-2020.csv
        3. world-population-forcast-2020-2050.csv
    '''
    country_details=extract_from_csv('d:/Python for Data Engineering Project/Project1/Source Files/countries-continents-capitals.csv')
    population=extract_from_csv('d:/Python for Data Engineering Project/Project1/Source Files/world-population-by-country-2020.csv')
    
    #creating DataFrame for json files

    '''
    JSON Files
        1. continent.json
        2. currency.json
        3. names.json
    '''

    
    currency=extract_from_json('d:/Python for Data Engineering Project/Project1/Source Files/currency.json')
    country_names=extract_from_json('d:/Python for Data Engineering Project/Project1/Source Files/names.json')

    #creatimg DataFrame for Excel file

    '''
    Excel file
        1. countries_GDP.xlsx
    '''
    countries_GDP=extract_from_excel('d:/Python for Data Engineering Project/Project1/Source Files/countries_GDP.xlsx')


    #return all 7 dataframes
    return country_details,population,currency,country_names,countries_GDP


    

def extract_from_url(url):

    # finding exchange rate of all countries based on USD

    dataframe=pd.DataFrame(columns=["Country","Exchange_Rate_USD"])
    data=requests.get(url)
    data=bs4.BeautifulSoup(data.content,'html.parser')
    table=data.find_all('tbody')
    rows=table[0].find_all('tr')
    for r in rows:
        col=r.find_all('td')
        if len(col)!=0:
            data_dict={
                "Country":col[0].a.contents[0],"Exchange_Rate_USD":float(col[1].contents[0])
            }
            df1=pd.DataFrame([data_dict])
            dataframe=pd.concat([dataframe,df1],ignore_index=True)
    return dataframe
