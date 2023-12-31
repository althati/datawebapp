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


        # Open the CSV file with newline='' to handle new line characters
        with open(csv_path, 'r', newline='') as file:
            # Create a CSV reader with customized parameters
            csv_reader = csv.reader(file, delimiter=',', quotechar='"', quoting=3)

            # Read the header
            header = next(csv_reader)
            print(header)

            

            # Read data into a list
            data = [row for row in csv_reader]
            print(data)

        # Create a DataFrame
        df = pd.DataFrame(data, columns=header)

        # Clean quotes from the header
        df.columns = df.columns.str.strip('"')

        # Clean quotes from DataFrame
        print("Clean quotes from DataFrame...")
        df = df.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)


        print("Loading file to table...")
        # Write the DataFrame to the PostgreSQL table
        df.to_sql(name='rhood_csv', schema='APP',con=engine, if_exists='append', index=False)

        # Close the engine
        engine.dispose()

            
                           
        print("Move file to archive...")
        shutil.move(csv_path, 'data/robinhood/archive/csv/')
        print("file to archived...")