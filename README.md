# Data-Engineering-Project-1

# Project Overview
This data engineering project involves extracting, transforming, and loading (ETL) data from various sources to create a comprehensive dataset for country analysis. It is divided into three main components:

Extract (extract.py):
Reads data from different file formats such as CSV, Excel, and JSON.
Downloads a zip file from GitHub containing source files, extracts the files, and creates DataFrames for further processing.
Fetches exchange rates for all countries based on USD from a specified URL(https://www.theglobaleconomy.com/rankings/Dollar_exchange_rate/).

Transform (transform.py):
Processes and cleans the extracted data to create structured datasets.
Renames columns, trims whitespace, and handles data type conversions.
Performs specific transformations on individual DataFrames (e.g., country_details, population, currency, country_names, countries_GDP).
Joins the transformed DataFrames to create a master DataFrame (df).
Calculates additional metrics such as GDP per capita.
Reorganizes columns and drops unnecessary ones.

Load (load.py):
Utilizes the transform() function from transform.py to obtain the master DataFrame.
Writes the final cleaned dataset to a CSV file (final.csv) in the specified directory (d:/Python for Data Engineering Project/Project1/Final File/).
Provides options for loading data into a SQL Server database.
db_connection(): Establishes a connection to the SQL Server database.
db_engine(): Creates a SQLAlchemy engine for database interaction.
load_to_db(): Loads the master DataFrame into the database table named Country_Analysis.

# Project Files

extract.py:
Contains functions for extracting data from CSV, Excel, JSON files, and a URL.
Downloads a zip file from GitHub, extracts the files, and creates individual DataFrames for each source file.

transform.py:
Performs data cleaning and transformation on the extracted DataFrames.
Creates a master DataFrame (df) by joining multiple DataFrames.
Calculates additional metrics such as GDP per capita.

load.py:
Provides functions for loading the transformed data.
Writes the final cleaned dataset to a CSV file (final.csv).
Supports loading data into a SQL Server database table (Country_Analysis).

# Usage

Data Extraction:
Run extract.py to download source files, extract data, and create individual DataFrames for each file and use webscrapping technique to load necessary data from URL.

Data Transformation:
Run transform.py to clean and transform the extracted data.
The master DataFrame (df) is created, containing comprehensive country analysis data.

Data Loading:
Run load.py to write the final dataset to a CSV file (final.csv).
Optionally, load the data into a SQL Server database using the load_to_db() function.

# Dependencies
Python 3.x
Required Python packages: pandas, requests, beautifulsoup4, openpyxl, pyodbc, sqlalchemy

# Notes
Ensure the necessary dependencies are installed.
Modify file paths and database connection details in the scripts according to your setup.
