import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
import shutil
import csv

# PostgreSQL connection parameters
db_params = {
    'user': 'appuser',
    'password': 'appuser',
    'host': 'localhost',
    'port': '5432',
    'database': 'MYANALYTICS'
}

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)

# Create a database engine
engine = create_engine(f'postgresql://{db_params["user"]}:"{db_params["password"]}"@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')


# Specify the directory path
directory_path = 'data/robinhood/csv'

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        csv_path = os.path.join(directory_path, filename)
        print("Processing file: {}".format(filename))
        # Open the PDF file in binary mode
        # Create a DataFrame from the CSV file
        df = pd.read_csv(csv_path, delimiter=',', quotechar='"', escapechar='\\',on_bad_lines='warn')
        
        df['Amount'] = df['Amount'].str.strip('()')
        df['Amount'] = df['Amount'].str.replace('[\$,]', '', regex=True).astype(float)

        df['Price'] = df['Price'].str.strip('()')
        df['Price'] = df['Price'].str.replace('[\$,]', '', regex=True).astype(float)
        
        df['Quantity'] = df['Quantity'].str.strip('()')
        
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
        

        df['Activity Date'] = pd.to_datetime(df['Activity Date']).dt.date

        print("Loading file to table...")
        # Write the DataFrame to the PostgreSQL table
        df.to_sql(name='rhood_csv2', schema='APP',con=engine, if_exists='append', index=False)

        # Close the engine
        engine.dispose()

            
                           
        print("Move file to archive...")
        shutil.move(csv_path, 'data/robinhood/archive/csv/')
        print("file to archived...")