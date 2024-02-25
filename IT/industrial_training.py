import pandas as pd
df1 = pd.DataFrame()

df1 = pd.read_csv("amazon.csv")
df2 = pd.DataFrame()
df2 = df1[["product_id","product_name","category","discounted_price","actual_price","discount_percentage","rating","rating_count"]]
print(df2["actual_price"])
df2["actual_price"] = df2["actual_price"].str[1:]
df2["actual_price"] =df2["actual_price"].replace(",","",regex=True)
df2["discounted_price"] = df2["discounted_price"].str[1:]
df2["discounted_price"] =df2["discounted_price"].replace(",","",regex=True)
df2["rating_count"] =df2["rating_count"].replace(",","",regex=True)
df2["discount_percentage"]=df2["discount_percentage"].replace("%","",regex=True)
df2["product_name"]=df2["product_name"].str[0:20]
print(df2)

df2.to_csv("clean_amazon3.csv")
