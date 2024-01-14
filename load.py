from transform import transform
import pandas as pd
import pyodbc
import urllib
import sqlalchemy as sa


def load_to_file():
    dataframe=transform()
    dataframe.to_csv('d:/Python for Data Engineering Project/Project1/Final File/final.csv',index=False)

def db_connection():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-G7H3F97;"
                      "Database=practice;"
                      "uid=testuser;""pwd=testuser;"
                      "TrustServerCertificate=yes;")

    cursor = cnxn.cursor()
    return cursor

def db_engine(): 
    conn= urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+'DESKTOP-G7H3F97'+';DATABASE='+'practice'+';UID='+'testuser'+';PWD='+ 'testuser')
    engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    return engine

def load_to_db():
    dataframe=transform()
    engine=db_engine()
    dataframe.to_sql('Country_Analysis',engine,index=False,if_exists="replace")

#load_to_db()
    