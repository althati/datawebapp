import pandas as pd
from sqlalchemy import create_engine
import psycopg2

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
table_name = '"APP".rhood_csv2'
value_to_search = "('Buy','Sell')"
#symbol_value2 = "'AAPL'"
groups = []

# Load data from the PostgreSQL table into a DataFrame
symbol_df = pd.read_sql(f'select distinct "Instrument" from {table_name} where "Trans Code" in {value_to_search} order by "Instrument"', engine)
for index, row in symbol_df.iterrows():
    # Initialize variables
    current_group = None
    # Load data from the PostgreSQL table into a DataFrame
    #print(row['Instrument'])
    symbol_value = "'"+row['Instrument']+"'"
    df = pd.read_sql(f'select *,EXTRACT(YEAR FROM "Activity Date") AS extracted_year from {table_name} where "Trans Code" in {value_to_search} and "Instrument" = {symbol_value} order by "Instrument","Activity Date","Trans Code"', engine)
    # Define a custom aggregation function
    def custom_aggregation(series):
        return '|'.join(series.astype(str))



    # Iterate through each row
    for index, row in df.iterrows():
        #print(row['Instrument'])
        if row['Trans Code'] == 'Buy' and current_group is None:
            # Create a new group
            current_group = []
        if current_group is not None:
            # Add the row to the current group
            current_group.append(row)
            next_index = index + 1
            if next_index < len(df):
                None
            else:
                groups.append(current_group)
        if row['Trans Code'] == 'Sell':
            # If 'Sell' is encountered, add the group to the list
                
                next_index = index + 1
                if next_index < len(df):
                    next_row = df.loc[next_index]
                    if next_row['Trans Code'] == 'Buy':
                        if current_group is not None:
                            groups.append(current_group)
                        current_group = None



#print(pd.DataFrame(groups))
# If you want to write each group to a separate table
for i, group in enumerate(groups):
    group_df = pd.DataFrame(group)
    #print(group_df)
    group_df.to_sql(name='rhood_csv4', schema='APP',con=engine, if_exists='append', index=False)
    #print(group_df)
    new_df = group_df.groupby(['Instrument','Trans Code']).agg({'extracted_year': custom_aggregation,'Quantity': 'sum', 'Amount': 'sum' }).reset_index()
    new_df['group_number'] = i
    #print(new_df)
    new_df.to_sql(name='rhood_csv3', schema='APP',con=engine, if_exists='append', index=False)
    #print(f'Group {i + 1} data written to table {table_name}')
    #appended_df = pd.concat(new_df, ignore_index=True)
# Close the engine
#engine.dispose()

#print(new_df)
    
print("done......")