import camelot

# PDF file to extract tables from
file = "data/sample.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file, pages='6')

print(tables)
# number of tables extracted
print("Total tables extracted:", tables.n)

