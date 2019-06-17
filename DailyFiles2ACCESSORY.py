import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Accessory\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Accessory\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Accessory\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Accessory\daily/'
files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Accessory\export\Master.xlsx', index=False))


import numpy as np
import pyodbc
import pandas as pd
import warnings

##### SETTINGS
pd.set_option('display.max_columns', 200000)
pd.set_option('display.width', 200000)
pd.options.display.max_colwidth = 200

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RD1\RD1;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

##### WARNINGS
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Accessory\export\Master.xlsx")


##############################################################################################################################
############ Datatypes
##############################################################################################################################

try:
    df['SalesCode'] = df["SalesPersonCode"]
except:
    df['SalesCode'] = "not found"

try:
    df['TransactionID'] = df['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['TransactionID'] = "not found"

try:
    df['InvoiceNumber'] = df['InvoiceNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['InvoiceNumber'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['BAN'] = df['BAN'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SalesCode'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['ActivityType'] = df['ActivityType'].astype(np.str)
except:
    df['ActivityType'] = "not found"

try:
    df['MSISDN'] = df['MSISDN'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MSISDN'] = "not found"

try:
    df['OrderID'] = df['OrderID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['OrderID'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['SalesCode'] = df['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SalesCode'] = "not found"

try:
    df['LineOfServiceID'] = df['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['LineOfServiceID'] = "not found"

try:
    df['Source'] = df['Source'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['Source'] = "not found"

try:
    df['StoreID'] = df['StoreID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['StoreID'] = "not found"

try:
    df['SAPTransTypeCode'] = df['SAPTransTypeCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SAPTransTypeCode'] = "not found"

try:
    df['ProxyID'] = df['ProxyID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProxyID'] = "not found"

try:
    df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
    df["Month"] = pd.to_datetime(df["Month"].fillna(0))
except:
    df['Month'] = 0

try:
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
except:
    df['TransactionDate'] = 0

try:
    df['MSRP'] = df['MSRP'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['MSRP'] = 0

try:
    df['SellingPrice'] = df['SellingPrice'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['SellingPrice'] = 0.0

try:
    df['CustomerPaidAmt'] = df['CustomerPaidAmt'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['CustomerPaidAmt'] = 0.0

try:
    df['CommissionAmount'] = df['CommissionAmount'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['CommissionAmount'] = 0.0

try:
    df['QTY'] = df['QTY'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['QTY'] = 0.0


##############################################################################################################################
############ Database
##############################################################################################################################

# ## DATABASE
# cursor = cnxn.cursor()
# for index,row in df.iterrows():
#     cursor.execute("INSERT INTO [Test].[dbo].[DAILY-ACCESSORY] ([TransactionID], [MasterDealerCode], [CheckNumber], [Month], [SalesCode], [TransactionDate], [StoreID], [InvoiceNumber], [MSRP], [POSType], [ActivityType], [SellingPrice], [CustomerPaidAmt], [SKU], [IMEI], [LineOfServiceID], [BAN], [MSISDN], [SAPTransTypeCode], [ProductCategory], [ProductDescription], [QTY], [Source], [ProxyID], [OrderID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     , row['TransactionID'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SalesCode'], row['TransactionDate'], row['StoreID'], row['InvoiceNumber'], row['MSRP'], row['POSType'], row['ActivityType'], row['SellingPrice'], row['CustomerPaidAmt'], row['SKU'], row['IMEI'], row['LineOfServiceID'], row['BAN'], row['MSISDN'], row['SAPTransTypeCode'], row['ProductCategory'], row['ProductDescription'], row['QTY'], row['Source'], row['ProxyID'], row['OrderID'])
# cnxn.commit()
# cursor.close()
# print("done")


## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-ACCESSORY] ([TransactionID], [MasterDealerCode], [CheckNumber], [Month], [SalesCode], [TransactionDate], [StoreID], [InvoiceNumber], [MSRP], [POSType], [ActivityType], [SellingPrice], [CustomerPaidAmt], [SKU], [IMEI], [LineOfServiceID], [BAN], [MSISDN], [SAPTransTypeCode], [ProductCategory], [ProductDescription], [QTY], [Source], [ProxyID], [OrderID],[CommissionAmount]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['TransactionID'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SalesCode'], row['TransactionDate'], row['StoreID'], row['InvoiceNumber'], row['MSRP'], row['POSType'], row['ActivityType'], row['SellingPrice'], row['CustomerPaidAmt'], row['SKU'], row['IMEI'], row['LineOfServiceID'], row['BAN'], row['MSISDN'], row['SAPTransTypeCode'], row['ProductCategory'], row['ProductDescription'], row['QTY'], row['Source'], row['ProxyID'], row['OrderID'], row['CommissionAmount'])
cnxn.commit()
cursor.close()
print("done")