import pandas as pd
# df = pd.DataFrame()
# df = pd.read_csv("housing.csv")
# df2 = df[["District Name","Rural/Urban","Total Number of households","Total Number of Livable","Total Number of Dilapidated","Latrine_premise"]]
# print(df2)
# df2.to_csv("clean_housing.csv")

df = pd.DataFrame()
df = pd.read_csv("clean_housing.csv")
print(df)