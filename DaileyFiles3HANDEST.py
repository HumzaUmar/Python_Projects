import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Handset\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Handset\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Handset\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Handset\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Handset\export\Master.xlsx', index=False))


import numpy as np
import pyodbc
import pandas as pd
import warnings

##### SETTINGS
pd.set_option('display.max_columns', 200000)
pd.set_option('display.width', 200000)
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RD1\RD1;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

##### WARNINGS
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Handset\export\Master.xlsx")

try:
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
except:
    df["TransactionDate"] = 0

try:
    df['TransactionID'] = df['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["TransactionID"] = "not found"


try:
    df['DiscountChargeBack'] = df['DiscountChargeBack'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["DiscountChargeBack"] = 0.0

try:
    df['StoreID'] = df['StoreID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["StoreID"] = "not found"

try:
    df['InvoiceNumber'] = df['InvoiceNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["InvoiceNumber"] = "not found"

try:
    df['SalesPersonCode'] = df['SalesPersonCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["SalesPersonCode"] = "not found"

try:
    df['MSISDN'] = df['MSISDN'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["MSISDN"] = "not found"

try:
    df['BAN'] = df['BAN'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["BAN"] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["IMEI"] = "not found"

try:
    df['SKU'] = df['SKU'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["SKU"] = "not found"

try:
    df['POSType'] = df['POSType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["POSType"] = "not found"

try:
    df['ActivityType'] = df['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["ActivityType"] = "not found"

try:
    df['LineOfServiceID'] = df['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["LineOfServiceID"] = "not found"

try:
    df['SAPTransTypeCode'] = df['SAPTransTypeCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["SAPTransTypeCode"] = "not found"

try:
    df['ProductCategory'] = df['ProductCategory'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["ProductCategory"] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["MasterDealerCode"] = "not found"

try:
    df['Month'] = df['Month'].str.replace("(", "").str.replace(")", "")
    df["Month"] = pd.to_datetime(df["Month"].fillna(0))
except:
    df["Month"] = 0

try:
    df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["CheckNumber"] = "not found"

try:
    df['Source'] = df['Source'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["Source"] = "not found"

try:
    df['OverrideReason'] = df['OverrideReason'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["OverrideReason"] = "not found"

try:
    df['QTY'] = df['QTY'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["QTY"] = 0.0

try:
    df['EIPIndicator'] = df['EIPIndicator'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["EIPIndicator"] = 0.0

try:
    df['ReturnCode'] = df['ReturnCode'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["ReturnCode"] = 0.0

try:
    df['EIP1stPayment'] = df['EIP1stPayment'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["EIP1stPayment"] = 0.0

try:
    df['EIPPlanID'] = df['EIPPlanID'].fillna(0).astype(np.int64)
    df['EIPPlanID'] = df['EIPPlanID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df["EIPPlanID"] = "not found"
    
try:
    df['MSRP'] = df['MSRP'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["MSRP"] = 0.0
    
try:
    df['SellingPrice'] = df['SellingPrice'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["SellingPrice"] = 0.0


try:
    df['CustomerPaidAmt'] = df['CustomerPaidAmt'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["CustomerPaidAmt"] = 0.0
    
try:
    df['PriceOffered'] = df['PriceOffered'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["PriceOffered"] = 0.0

try:
    df['OverrideReason'] = df['OverrideReason'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df["OverrideReason"] = 0.0


## DATABASE
cursor = cnxn.cursor()
for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-HANDSET] ([TransactionID], [TransactionDate], [StoreID], [InvoiceNumber], [MSRP], [SellingPrice], [CustomerPaidAmt], [PriceOffered], [SalesPersonCode], [SKU], [IMEI], [BAN], [MSISDN], [POSType], [ActivityType], [LineOfServiceID], [SAPTransTypeCode], [ProductCategory], [ProductDescription], [QTY], [OverrideReason], [ReturnCode], [EIPIndicator], [EIP1stPayment], [EIPPlanID], [MasterDealerCode], [Month], [CheckNumber], [Source], [DiscountChargeBack]) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                   ,row['TransactionID'], row['TransactionDate'], row['StoreID'], row['InvoiceNumber'], row['MSRP'], row['SellingPrice'], row['CustomerPaidAmt'], row['PriceOffered'], row['SalesPersonCode'], row['SKU'], row['IMEI'], row['BAN'], row['MSISDN'], row['POSType'], row['ActivityType'], row['LineOfServiceID'], row['SAPTransTypeCode'], row['ProductCategory'], row['ProductDescription'], row['QTY'], row['OverrideReason'], row['ReturnCode'], row['EIPIndicator'], row['EIP1stPayment'], row['EIPPlanID'], row['MasterDealerCode'], row['MasterDealerCode'], row['Month'], row['Source'], row["DiscountChargeBack"])
cnxn.commit()
cursor.close()
print("done")


