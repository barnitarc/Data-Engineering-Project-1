from extract import extract_from_files,extract_from_url
import pandas as pd

#Now we are going to transform each dataframe to structured and clean data
def transform():
    #loading extracted data from files
    country_details,population,currency,country_names,countries_GDP=extract_from_files()
    #loading extracted data from URL
    exchange_rate=extract_from_url('https://www.theglobaleconomy.com/rankings/Dollar_exchange_rate/')

    ''' transforming country_details dataframe
        1. renaming column "Country/Territory"
        2. trimming all 3 columns
    '''
    country_details=country_details.rename(columns={"Country/Territory":"Country"}).dropna()
    country_details["Country"]=country_details["Country"].str.strip()
    country_details["Capital"]=country_details["Capital"].str.strip()
    country_details["Continent"]=country_details["Continent"].str.strip()
    
    '''
        transforming population dataframe
        1. select the following columns from the dataframe { 'ï»¿no','Country (or dependency)',
        'Population 2020','Density  (P/KmÂ²)', 'Land Area (KmÂ²)', 'World Share'}
        2. renaming all column names
        3. remove ',' from Population_2020, Density and Land area columns
        4. remove '%' from World Share column
        5. change datatypes 
    
    '''
    population=population.iloc[:,[0,1,2,5,6,11]]
    new_columns={
        'ï»¿no':"Rank_in_population",
        'Country (or dependency)':"Country",
        'Population 2020':'Population_2020',
        'Density  (P/KmÂ²)':'Density', 
        'Land Area (KmÂ²)':"Land_area", 
        'World Share':'World_share'
    }
    population=population.rename(columns=new_columns)

    population['Population_2020']=population['Population_2020'].str.replace(',','')
    population['Density']=population['Density'].str.replace(',','')
    population['Land_area']=population['Land_area'].str.replace(',','')
    population['World_share']=population['World_share'].str.replace('%','')

    new_dtypes={'Rank_in_population':int, 'Country':str, 'Population_2020':int, 'Density':float,
           'Land_area':float, 'World_share':float}
    population=population.astype(new_dtypes)

    '''
        joining transformed dataframes to create one master dataframe
    '''

    df=population.merge(country_details,on="Country",how='left')
    df=df.merge(exchange_rate,on="Country",how='left')
    df1=currency.merge(country_names,on='Country_Code')
    df=df.merge(df1,right_on="Country_Name",left_on="Country",how='left')
    
    df=df.drop(columns=['Country_Name'],axis=1)

    df=df.merge(countries_GDP,on="Country",how='left')
    df=df.rename(columns={'Rank':'Rank_in_GDP'})
    df['Rank_in_GDP']=df['Rank_in_GDP'].astype('Int64')

    '''
        create new column 'GDP_by_capita'
    '''
    df['GDP_by_capita']=round(df['IMF_GDP']/df['Population_2020'],2)

    #rearrange the columns in master dataframe
    df = df.reindex(columns=['Country_Code','Country', 'Capital', 'Continent','Currency', 'Exchange_Rate_USD','Rank_in_population', 'Population_2020', 
           'Rank_in_GDP', 'IMF_GDP', 'UN_GDP', 'GDP_by_capita','Density',
           'Land_area', 'World_share'])
    # drop all rows where country code is missing
    df=df.dropna(subset='Country_Code')
    return df

