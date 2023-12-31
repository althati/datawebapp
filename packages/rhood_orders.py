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
with open('data/orders.txt', 'r') as input_file:
    # Read the entire contents of the file
    lines = input_file.readlines()

#print(lines)
# Process the data to group every three rows into one row with three columns
grouped_data = [lines[i:i+5] for i in range(0, len(lines), 5)]
#print(grouped_data)
# Create a DataFrame from the grouped data
df = pd.DataFrame([group for group in grouped_data], columns=['Column1', 'Column2', 'Column3','Column4','Column5'])

df_cleaned = df.applymap(lambda x: x.replace('\n', '') if x is not None else x)
#df_cleaned['date'] = df_cleaned['Column2'].str.split(' · ').str[1]
#df_cleaned['type'] = df_cleaned['Column1'].str.split(' ').str[0]
df_cleaned['amount'] = df_cleaned['Column3']
df_cleaned['stock'] = df_cleaned['Column1'].str.split(' ').str[0]
df_cleaned['quantity'] = df_cleaned['Column4'].str.split(' ').str[0]

print(df_cleaned)
df_new = df_cleaned[['stock','amount','quantity']]

df_new['amount'] = df_new['amount'].str.replace('[\$,]', '', regex=True).astype(float)
df_new['quantity'] = df_new['quantity'].astype(float)

# Display the DataFrame
print(df_new)


print("Writing to PostgreSQL database...")
df_new.to_sql(name='rhood_today', schema='APP',con=engine, if_exists='replace', index=False)

print("Closing connection...")
# Close the connection
conn.close()

print("Done.")
                            