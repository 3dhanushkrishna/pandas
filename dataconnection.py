import pandas as pd
import sqlite3
connection = sqlite3.connect("college.db")
df = pd.read_sql_query("select * from STUDENT",connection)
# print(df.head())
print(df.tail(1))