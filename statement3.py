import pandas as pd
df = pd.DataFrame()
df = pd.read_csv("census2011sql.csv")
print(df["District"])