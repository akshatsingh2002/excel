import pandas as pd
df = pd.DataFrame()
df = pd.read_csv("census2011.csv")
# print(df)
f = open("Telangana.txt","r")
lst = f.readlines()

for i in range(0,639):
    if df.iloc[i,2] in lst or df.iloc[i,2]+"\n" in lst:
        df.iloc[i,1] = "Telangana"

print(df["State/UT"])
df.to_csv("temp.csv")
print(lst)