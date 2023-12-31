import PyPDF2
import pandas as pd
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

#dtypes = {'symbol': 'str', 'trn': 'str', 'date': 'date', 'qty': 'float64', 'price':'float64', 'debit' :'float64', 'credit':'float64','description':'str','filename':'str'}

# Function to check if an object is a date
def is_date(obj):
    try:
        datetime.strptime(str(obj), '%m/%d/%Y')
        return True
    except ValueError:
        return False



# Specify the directory path
directory_path = 'data/robinhood'

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(directory_path, filename)
        print("Processing file: {}".format(filename))
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Extract text from all pages
            text = ''
            for indx, page in enumerate(pdf_reader.pages):
                if 'Account Activity' in page.extract_text():
                    page = pdf_reader.pages[indx]
                    text = page.extract_text()
                    #print("************************text************************")
                    #print(text)
                    # Convert text into a DataFrame (example splitting by newline)
                    lines = text.split('\n')
                    #print("************************lines************************")
                    #print(lines)

                    # Iterate through the list using enumerate()
                    lines2 = []
                    for index, value in enumerate(lines):
                        #print(f'Index: {index}, Value: {value}')
                        if 'Margin' in value and 'Aggregated' not in value:
                            print(value)
                            value2 = value.split(' ')

                            # Filter the array to get only date elements
                            date_elements = [elem for elem in value2 if is_date(elem)]
                            #print(date_elements)
                            if len(date_elements) == 1:
                                #index = value2.index("Margin")  
                                index = next((index for index, s in enumerate(value2) if 'Margin' in s), -1)
                                #print(f'The index of "Margin" in the list is: {index}')
                                #print(value2[index-1])
                                #print(value2)
                                #print(value2[index+1])
                                if value2[index+1] == 'ACH':
                                    lines2.append({'symbol': 'ACH Deposit' if 'Deposit' in value2[index-1] else ('ACH Withdrawal' if 'Withdrawal' in value2[index-1] else 'ACH Cancel'), 'trn': 'ACH', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :None, 'credit':value2[index+3],'description':None,'filename':filename})
                                elif value2[index+1] == 'COIN':
                                    lines2.append({'symbol': 'COIN', 'trn': 'COIN', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :None, 'credit':value2[index+3],'description':None,'filename':filename})
                                elif value2[index+1] == 'Buy' and 'Reinvestment' in value2[index-1]:
                                    lines2.append({'symbol': value2[index-1].replace('Reinvestment',''), 'trn': 'Buy', 'date': value2[index+2], 'qty': value2[index+3], 'price':value2[index+4], 'debit' :value2[index+5], 'credit':None,'description':'Dividend Reinvestment','filename':filename})
                                elif value2[index+1] == 'Buy' and 'Reinvestment' not in value2[index-1]:
                                    lines2.append({'symbol': re.sub(r'[^a-zA-Z]', '', value2[index-1]), 'trn': 'Buy', 'date': value2[index+2], 'qty': value2[index+3], 'price':value2[index+4], 'debit' :value2[index+5], 'credit':None,'description':None,'filename':filename})
                                elif value2[index+1] == 'Sell':
                                    lines2.append({'symbol': re.sub(r'[^a-zA-Z]', '', value2[index-1]), 'trn': 'Sell', 'date': value2[index+2], 'qty': value2[index+3], 'price':value2[index+4], 'debit' :None, 'credit':value2[index+5],'description':None,'filename':filename})
                                elif value2[index+1] == 'SLIP':
                                    lines2.append({'symbol': value2[index-1].split('%')[1] if '%' in value2[index-1] else value2[index-1].replace('Payment',''), 'trn': 'SLIP', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :None, 'credit':value2[index+3],'description':None,'filename':filename})
                                elif value2[index+1] == 'GOLD':
                                    lines2.append({'symbol': 'Gold Subscription Fee', 'trn': 'GOLD', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :value2[index+3], 'credit':None,'description':None,'filename':filename})
                                elif value2[index+1] == 'MINT':
                                    lines2.append({'symbol': 'Margin Interest', 'trn': 'MINT', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :value2[index+3], 'credit':None,'description':None,'filename':filename})
                                elif value2[index+1] == 'AFEE':
                                    lines2.append({'symbol': 'ADR Fee', 'trn': 'AFEE', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :value2[index+3], 'credit':None,'description':None,'filename':filename})
                                elif value2[index+1] == 'DFEE':
                                    lines2.append({'symbol': 'ADR Fee', 'trn': 'DFEE', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' :value2[index+3], 'credit':None,'description':None,'filename':filename})
                                elif value2[index+1] == 'CDIV':
                                    lines2.append({'symbol': re.sub(r'[^a-zA-Z]', '', value2[index-1]), 'trn': 'CDIV', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':value2[index+3],'description':None,'filename':filename})
                                elif value2[index+1] == 'MDIV':
                                    lines2.append({'symbol': re.sub(r'[^a-zA-Z]', '', value2[index-1]), 'trn': 'MDIV', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':value2[index+3],'description':None,'filename':filename})
                                elif value2[index+1] == 'CIL':
                                    lines2.append({'symbol': re.sub(r'[^a-zA-Z]', '', value2[index-1]), 'trn': 'CIL', 'date': value2[index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':value2[index+3],'description':None,'filename':filename})
                                else:
                                    lines2.append({'symbol': None, 'trn': value2[index+1], 'date': value2[index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':None,'description':None,'filename':filename})
                        if 'Sweep' in value:
                            #print(value)
                            value2 = value.split(' ')
                            date_elements = [elem for elem in value2 if is_date(elem)]
                            if len(date_elements) == 1:
                                sweep_index = value2.index("Sweep")
                                if value2[sweep_index+1] == 'INT':
                                    lines2.append({'symbol': 'Interest Payment', 'trn': 'INT', 'date': value2[sweep_index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':value2[sweep_index+3],'description':None,'filename':filename})
                                else:
                                    lines2.append({'symbol': value2[sweep_index-1], 'trn': value2[sweep_index+1], 'date': value2[sweep_index+2], 'qty': None, 'price':None, 'debit' : None, 'credit':None,'description':None,'filename':filename})

                        
                                            

                            
                    #print("************************lines2************************")
                    #print(lines2)

                    
                    df = pd.DataFrame(lines2)
                    #print("************************df************************")
                    # Print the DataFrame
                    #print(df)

                    print("Writing to PostgreSQL database...")
                    df.to_sql(name='rhood', schema='APP',con=engine, if_exists='append', index=False)

                    print("Closing connection...")
                    # Close the connection
                    conn.close()

                    print("Done.")
                            
        print("Move file to archive...")
        shutil.move(pdf_path, 'data/robinhood/archive/')
        print("file to archived...")