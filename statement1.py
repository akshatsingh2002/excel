import pandas as pd
df = pd.DataFrame()
df = pd.read_csv("census_2011.csv")
print(df)
# df.drop('State name')
df2 = df.filter(["State name","District name","Population","Male","Female","Literate","Male_Literate","Female_Literate","Rural_Households","Urban_Households","Households","Age_Group_0_29Age_Group_30_49","Age_Group_50","Age not stated"])
df2.to_csv("census2011.csv")
print(df2)