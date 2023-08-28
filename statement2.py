import pandas as pd
df=pd.DataFrame()
df = pd.read_csv("census2011.csv")
print(df)
df.rename(columns={'State name':'State/UT','District name':'District','Male_Literate':'Literate_Male','Female_Literate':'Literate_Female','Rural_Household':'Household_Rural','Urban_Household':'Household_Urban','Age_Group_0_29':'Young_and_Adult','Age_Group_30_49': 'Middle_Aged','Age_Group_50':'Senior_Citizen','Age not stated':'Age_Not_Stated'},inplace="True")
print(df)
df.to_csv("census2011Sql.csv")