import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import yfinance as yf

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

df = pd.read_csv('data/robinhood/current_holdings.csv', delimiter=',')

print("Writing to PostgreSQL database...")
df.to_sql(name='current_holdings', schema='APP',con=engine, if_exists='append', index=False)

print("Closing connection...")
# Close the connection
conn.close()

print("Done.")