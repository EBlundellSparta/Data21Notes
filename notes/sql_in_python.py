import sqlalchemy
from pprint import pprint

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'

engine = sqlalchemy.create_engine(f'mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}')

connection = engine.connect()

result = engine.execute('SELECT * FROM Products;')
print(result.keys())

# first_row = result.fetchone()
# pprint(first_row)

# all_rows = result.fetchall()
# pprint(all_rows)

# many_rows = result.fetchmany(2)
# pprint(many_rows)

# first_row = result.fetchone()
# pprint(f"Product Name: {first_row[1]}, CategoryID: {first_row[3]}")

# First row and second column
# all_rows = result.fetchall()
# pprint(f"Product Name: {all_rows[0][1]}")

# Rows 1 to 5 and prints the second column
# all_rows = result.fetchall()[0:5]
# for i in all_rows:
#     print(i[1])

