import pandas as pd
import psycopg2
from sqlalchemy import create_engine

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



# Replace 'your_table' and '/path/to/your/file.csv' with actual table and file path
table_name = '"APP".hold_view'
file_path = 'data/robinhood/holdview2.csv'

# Connect to the database
conn = psycopg2.connect(**db_params)

# Query to fetch data from the table
query = f"SELECT * FROM {table_name} where unrealized_profit < 0;"

# Use pandas to read the query result into a DataFrame
df = pd.read_sql(query, conn)

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)

# Close the connection
conn.close()
