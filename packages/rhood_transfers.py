import re
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os
import shutil
from datetime import datetime


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


# Open the text file for reading
with open('data/plain.txt', 'r') as input_file:
    # Read the entire contents of the file
    lines = input_file.readlines()

#print(lines)
# Process the data to group every three rows into one row with three columns
grouped_data = [lines[i:i+4] for i in range(0, len(lines), 4)]
#print(grouped_data)
# Create a DataFrame from the grouped data
df = pd.DataFrame([group for group in grouped_data], columns=['Column1', 'Column2', 'Column3','Column4'])

df_cleaned = df.applymap(lambda x: x.replace('\n', '') if x is not None else x)

df_cleaned['date'] = df_cleaned['Column2'].str.split(' · ').str[1]
df_cleaned['type'] = df_cleaned['Column1'].str.split(' ').str[0]
df_cleaned['amount'] = df_cleaned['Column3'].str.replace('[\$,]', '', regex=True).str.replace('-', '').str.replace('+', '')


# Display the DataFrame
print(df_cleaned)