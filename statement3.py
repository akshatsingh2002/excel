import pandas as pd
df = pd.DataFrame()
df = pd.read_csv("census2011.csv")
for i in df["District"]:
    i = i.split()
    if "AND" in i:
        print(df["District"])