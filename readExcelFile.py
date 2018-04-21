
import pandas as pd
import xlrd

xl = pd.read_excel('PYTHON_SAMPLE_FILE.xlsx', sheetname='Sheet1')
# print(xl.head())
result = pd.DataFrame()
for index, row in xl.iterrows():
    if row not in result:
        result.append(row)
print(result.head())




