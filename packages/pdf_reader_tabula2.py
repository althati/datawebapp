import tabula
import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from pypdf import PdfReader


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

# read PDF file
data = tabula.read_pdf("data/sample.pdf", pages=8, multiple_tables=True)

print(data)

df = data[0]
print(df)
#print(df.index)
#print(df.loc[0])

print("Writing to PostgreSQL database...")
df.to_sql(name='rhood', schema='APP',con=engine, if_exists='replace', index=False)

print("Closing connection...")
# Close the connection
conn.close()

print("Done.")