import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Spiff\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
# ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Prepay Residual\{}".format(filename)
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Spiff\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Spiff\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Spiff\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Spiff\export\Master.xlsx', index=False))


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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Spiff\export\Master.xlsx")

try:
    df['ServiceUniversalID'] = df['ServiceUniversalID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ServiceUniversalID'] = "not found"

try:
    df['CAPID'] = df['CAPID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CAPID'] = "not found"

try:
    df['CAPDescription'] = df['CAPDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CAPDescription'] = "not found"

try:
    df['SpiffID'] = df['SpiffID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SpiffID'] = "not found"

try:
    df['SpiffDescription'] = df['SpiffDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SpiffDescription'] = "not found"

try:
    df['DealerCode'] = df['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['DealerCode'] = "not found"

try:
    df['DealerName'] = df['DealerName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['DealerName'] = "not found"

try:
    df['PlanCode'] = df['PlanCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['PlanCode'] = "not found"

try:
    df['MarketCode'] = df['MarketCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MarketCode'] = "not found"

try:
    df['CommMarketCode'] = df['CommMarketCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CommMarketCode'] = "not found"

try:
    df['ProductType'] = df['ProductType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProductType'] = "not found"

try:
    df['ActivityType'] = df['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ActivityType'] = "not found"

try:
    df['SameMonth'] = df['SameMonth'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SameMonth'] = "not found"

try:
    df['LineOfServiceID'] = df['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['LineOfServiceID'] = "not found"

try:
    df['ServiceNumber'] = df['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ServiceNumber'] = "not found"

try:
    df['CustomerName'] = df['CustomerName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CustomerName'] = "not found"

try:
    df['SIMM'] = df['SIMM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIMM'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['BAN'] = df['BAN'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['BAN'] = "not found"

try:
    df['CreditType'] = df['CreditType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CreditType'] = "not found"

try:
    df['CreditClass'] = df['CreditClass'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CreditClass'] = "not found"

try:
    df['SpiffGroup'] = df['SpiffGroup'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SpiffGroup'] = "not found"

try:
    df['HOTI'] = df['HOTI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['HOTI'] = "not found"

try:
    df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SubDealerID'] = "not found"

try:
    df['ProductCatDescription'] = df['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProductCatDescription'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['Month'] = df['Month'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['Month'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['AdditionalDescription'] = df['AdditionalDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['AdditionalDescription'] = "not found"

try:
    df['AccountTypeID'] = df['AccountTypeID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['AccountTypeID'] = "not found"

try:
    df['AccountSubTypeID'] = df['AccountSubTypeID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['AccountSubTypeID'] = "not found"

try:
    df['ActivatingStoreID'] = df['ActivatingStoreID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ActivatingStoreID'] = "not found"

try:
    df['ProInstall'] = df['ProInstall'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProInstall'] = "not found"

try:
    df['Id'] = df['Id'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['Id'] = "not found"

try:
    df['Payout'] = df['Payout'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['Payout'] = 0.0

try:
    df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

try:
    df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['MonthlyAccess'] = 0.0

try:
    df['ContractTerm'] = df['ContractTerm'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['ContractTerm'] = 0.0

default ="2010-10-01"

try:
    df["ActDate"] = pd.to_datetime(df["ActDate"].fillna(default))
except:
    df['ActDate'] = default

try:
    df["DeactDate"] = pd.to_datetime(df["DeactDate"].fillna(default))
except:
    df['DeactDate'] = default

try:
    df["LastUpgradeDate"] = pd.to_datetime(df["LastUpgradeDate"].fillna(default))
except:
    df['LastUpgradeDate'] = default

try:
    df["LastSuspendDate"] = pd.to_datetime(df["LastSuspendDate"].fillna(default))
except:
    df['LastSuspendDate'] = default

try:
    df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
    df["Month"] = pd.to_datetime(df["Month"].fillna(default))
except:
    df['Month'] = default

# print(df)

## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-SPIFF] ([ServiceUniversalID], [CAPID], [CAPDescription], [SpiffID], [SpiffDescription], [DealerCode], [DealerName], [MonthlyAccess], [PlanCode], [MarketCode], [CommMarketCode], [ProductType], [ActivityType], [ActDate], [DeactDate], [SameMonth], [LineOfServiceID], [ServiceNumber], [CustomerName], [SIMM], [IMEI],[BAN], [ContractTerm], [CreditType], [CreditClass], [LastSuspendDate], [SpiffGroup], [HOTI], [SubDealerID], [ProductCatDescription] , [MasterDealerCode], [Month], [CheckNumber], [AdditionalDescription], [AccountTypeID], [AccountSubTypeID], [LastUpgradeDate], [ActivatingStoreID], [ProInstall], [Id], [Payout],  [ContractID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['ServiceUniversalID'], row['CAPID'], row['CAPDescription'], row['SpiffID'], row['SpiffDescription'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['CommMarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['SameMonth'], row['LineOfServiceID'], row['ServiceNumber'], row['CustomerName'], row['SIMM'], row['IMEI'], row['BAN'], row['ContractTerm'], row['CreditType'], row['CreditClass'], row['LastSuspendDate'], row['SpiffGroup'], row['HOTI'], row['SubDealerID'], row['ProductCatDescription'], row['MasterDealerCode'], row['Month'], row['CheckNumber'], row['AdditionalDescription'], row['AccountTypeID'], row['AccountSubTypeID'], row['LastUpgradeDate'], row['ActivatingStoreID'], row['ProInstall'], row['Id'], row['Payout'], row['ContractID'])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-SPIFF] ([LastSuspendDate]) VALUES(?)", row["LastSuspendDate"])
cnxn.commit()
cursor.close()
print("done")
