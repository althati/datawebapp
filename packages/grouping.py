import pandas as pd
from sqlalchemy import create_engine

# Create a sample DataFrame
data = {'TransactionType': ['Buy','Sell','Buy','Buy','Buy','Sell','Buy','Sell','Buy','Sell','Buy','Buy','Sell','Sell','Buy','Buy'],
        'Year': ['2020', '2021', '2020', '2021', '2022', '2022', '2023', '2024', '2021', '2023', '2023', '2024', '2024', '2025', '2025', '2025'],
        'Quantity': [10, 5, 8, 15, 7, 5, 2, 3, 12, 10, 4, 5, 6, 7, 8, 9],
        'Amount': [100.0, 50.0, 80.0, 150.0, 70.0, 50.0, 20.0, 30.0, 120.0, 100.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]}



df = pd.DataFrame(data)
# Define a custom aggregation function
def custom_aggregation(series):
    return '|'.join(series.astype(str))
# Initialize variables
groups = []
current_group = None
# Iterate through each row
for index, row in df.iterrows():
    if row['TransactionType'] == 'Buy' and current_group is None:
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
    if row['TransactionType'] == 'Sell':
        # If 'Sell' is encountered, add the group to the list
            
            next_index = index + 1
            if next_index < len(df):
                next_row = df.loc[next_index]
                if next_row['TransactionType'] == 'Buy':
                    groups.append(current_group)
                    current_group = None
                    
            else:
                 groups.append(current_group)

# PostgreSQL connection parameters
db_params = {
    'host': 'your_host',
    'port': 'your_port',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_database'
}


appended_df = pd.DataFrame()
# If you want to write each group to a separate table
for i, group in enumerate(groups):
    group_df = pd.DataFrame(group)
    print(group_df)
    #new_df = group_df.groupby(['TransactionType']).agg({'Year': custom_aggregation,'Quantity': 'sum', 'Amount': 'sum', }).reset_index()
    #print(new_df)
    #group_df.to_sql(table_name, engine, index=False, if_exists='replace')
    #print(f'Group {i + 1} data written to table {table_name}')
    #appended_df = pd.concat(new_df, ignore_index=True)
# Close the engine
#engine.dispose()
