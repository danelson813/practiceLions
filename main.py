# practiceLions/main.py

import pandas as pd
import duckdb

from helpers.querys import query, query_sumb, query1, query_inc, query_sumt

ledger = pd.read_excel("data/Ledger 25.xlsx", usecols="A:H")
budget = pd.read_excel("data/Ledger 25.xlsx", sheet_name=1)
conn = duckdb.connect()

cur = conn.cursor()

query = query()
cur.sql(query)

query1 = query1()
cur.sql(query1)

expense = [(10 * i) for i in range(1, 37)]

results = [("Budget_line", "BUDGET", "Income", "Expense")]
for x in expense:
    if x in [60, 310]:
        continue
    row = (
        int(x),
        cur.sql(query_sumb(x)).fetchall()[0][0],
        cur.sql(query_inc(x)).fetchall()[0][0],
        cur.sql(query_sumt(x)).fetchall()[0][0],
    )
    # print(row)
    results.append(row)

df = pd.DataFrame(results)

df.to_excel("data/trial.xlsx", index=False)
