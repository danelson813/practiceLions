# practiceLions/main.py

import pandas as pd
import duckdb

ledger = pd.read_excel("data/Ledger 25.xlsx",usecols='A:H')

conn = duckdb.connect()

cur = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS transactions AS SElECT * FROM ledger;
"""
cur.sql(query)

query2 = '''
    SELECT * FROM transactions;
'''
data = cur.sql(query2).fetchall()
for item in data:
    print(item)
expense = [(10*i) for i in range(1,37)]
income = [(10*i+5) for i in range(1,37)]
print(income)
print(expense)
results = [('Budget_line', 'Income', 'Expense')]
for x in expense:
    query3 = f'''
        SELECT SUM(amount) FROM transactions 
        WHERE Budget_Line = {x+5}
    '''
    # row = (int(x), cur.sql(query3).fetchall()[0])
    # print(row)


    query = f'''
        SELECT SUM(amount) FROM transactions 
        WHERE Budget_Line = {x}
    '''
    row = (int(x),
           cur.sql(query3).fetchall()[0][0],
           cur.sql(query).fetchall()[0][0])
    # print(row)
    results.append(row)
for _ in results:
    print(_)

df = pd.DataFrame(results)
# print(df.info())
# print(df.head(10))
df.to_excel('data/trial.xlsx', index=False)
