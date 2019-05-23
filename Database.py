import os
import pandas as pd
import numpy as np
import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RD1\RD1;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)

path = os.getcwd()
files = os.listdir(r'C:\Users\RD1\Desktop\Task_Assigned\Serial Number 01-08-2018')
path_file =  r'C:\Users\RD1\Desktop\Task_Assigned\Serial Number 01-08-2018/'
files_xls = [f for f in files if f[-4:] == 'xlsx']
df = pd.DataFrame()

for f in files_xls:
    data = pd.read_excel(path_file+f)
    df = df.append(data)


df['SKUDescr'] = df['SKUDescr'].fillna(0).astype(np.str)
df['Item'] = df['Item'].fillna(0).astype(np.str)
df['Delivery(PackList)'] = df['Delivery(PackList)'].fillna(0).astype(np.str)
df['SKU'] = df['SKU'].fillna(0).astype(np.str)
df['PONumber'] = df['PONumber'].fillna(0).astype(np.str)
df['Cust/Store'] = df['Cust/Store'].fillna(0).astype(np.str)
df['IMEI/SerialNumber'] = df['IMEI/SerialNumber'].fillna(0).astype(np.str)
df['IMEI/SerialNumber'] = df['IMEI/SerialNumber'].apply(lambda x: '{0:0>15}'.format(x))

# print(df.to_excel(r'C:\Users\RD1\Desktop\Task_Assigned\Serial Number 01-08-2018\Master3.xlsx', index=False))

## DATABASE CONNECT
cursor = cnxn.cursor()
df4 = df
# df4 = df4.astype(str)
print(df4.dtypes)
for index, row in df4.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[Serial_asn] (CustStore, DeliveryPackList, IssueDate, Item, SKU, SKUDescr, IMEISerialNumber, PONumber) VALUES (?,?,?,?,?,?,?,?)"
        , str(row['Cust/Store']), str(row['Delivery(PackList)']), row['IssueDate'], str(row['Item']), str(row['SKU']), str(row['SKUDescr']), str(row['IMEI/SerialNumber']), str(row['PONumber']))

cnxn.commit()
cursor.close()