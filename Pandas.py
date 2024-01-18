import pandas as pd

# df = pd.read_excel("Data/practice_sheet.xlsx",sheet_name="Sheet1")
#
# # print(df)
# print(df.head(6))

df_csv = pd.read_csv('Data/departments.csv')

print(df_csv.describe())
