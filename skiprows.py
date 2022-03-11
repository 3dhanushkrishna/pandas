import pandas as pd
df = pd.read_csv("Student.csv" ,skiprows=[0,1])

print(df)