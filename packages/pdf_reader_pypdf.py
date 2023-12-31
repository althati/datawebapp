from pypdf import PdfReader
import pandas as pd
import tabula
import os

os.environ["JAVA_HOME"] = "/opt/homebrew/Cellar/openjdk/21.0.1/libexec/openjdk.jdk/Contents/Home"

pdf_reader = PdfReader('data/sample.pdf')

page_content = {}

for indx, page in enumerate(pdf_reader.pages):
    if 'Account Activity' in page.extract_text():
        page_content[indx] = page.extract_text()
        df = tabula.read_pdf("data/sample.pdf", pages='7', multiple_tables=True)
        print(df)

print(page_content)

#transactions = [line.strip() for line in pdf_text.split('\n') if 'Transaction' in line]



# Assuming you've parsed the data into a list of lists or a DataFrame
#data = [["Date", "Transaction", "Amount"]]  # Example data
#data.extend(parsed_transactions)

#df = pd.DataFrame(data)
#df.to_csv("robinhood_activity.csv", index=False)