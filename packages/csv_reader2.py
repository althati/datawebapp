import csv
import pandas as pd

# CSV file and table names
csv_file = 'data/robinhood/csv/e1c467a4-ae70-5107-862d-e4c077686931.csv'


# Open the CSV file with newline='' to handle new line characters
with open(csv_file, 'r', newline='') as file:
    # Create a CSV reader with customized parameters
    csv_reader = csv.reader(file, delimiter=',', quotechar='"', quoting=3)

    # Read the header
    header = next(csv_reader)

    # Read data into a list
    data = [row for row in csv_reader]

# Create a DataFrame
df = pd.DataFrame(data, columns=header)
