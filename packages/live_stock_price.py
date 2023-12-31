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



# Replace 'your_table' with the actual table name
table_name = '"APP".final_view'


# Load data from the PostgreSQL table into a DataFrame
symbol_df = pd.read_sql(f'select distinct stock from {table_name} where sell_price is null order by stock', engine)
lines = []

for index, row in symbol_df.iterrows():
    print(row['stock'])
    stock_symbol = row['stock']
    if stock_symbol != 'RIDE':
        stock_info = yf.Ticker(stock_symbol).info
        print(stock_info)
        if stock_info.get('currentPrice') is not None:
            current_stock_price = stock_info["currentPrice"]
            print(current_stock_price)
            lines.append({'symbol': stock_symbol, 'current_stock_price': current_stock_price})


df = pd.DataFrame(lines)
#print("************************df************************")
# Print the DataFrame
print(df)

print("Writing to PostgreSQL database...")
df.to_sql(name='live_stock_price', schema='APP',con=engine, if_exists='append', index=False)

print("Closing connection...")
# Close the connection
conn.close()

print("Done.")