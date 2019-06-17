import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Statement\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Statement\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Statement\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Statement\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Statement\export\Master.xlsx', index=False))


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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Statement\export\Master.xlsx")

try:
    df['ServiceUniversalID'] = df['ServiceUniversalID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ServiceUniversalID'] = "not found"

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
    df['ProductType'] = df['ProductType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProductType'] = "not found"

try:
    df['ActivityType'] = df['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ActivityType'] = "not found"

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
    df['PreToPostMigration'] = df['PreToPostMigration'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['PreToPostMigration'] = "not found"

try:
    df['CreditClass'] = df['CreditClass'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CreditClass'] = "not found"

try:
    df['HandSetOfferTypeIndicator'] = df['HandSetOfferTypeIndicator'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['HandSetOfferTypeIndicator'] = "not found"

try:
    df['SubdealerID'] = df['SubdealerID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SubdealerID'] = "not found"

try:
    df['ProdCatDescription'] = df['ProdCatDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProdCatDescription'] = "not found"

try:
    df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

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
    df['IsEligible'] = df['IsEligible'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['IsEligible'] = "not found"

try:
    df['NonCommissionableReason'] = df['NonCommissionableReason'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['NonCommissionableReason'] = "not found"

try:
    df['Source'] = df['Source'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['Source'] = "not found"

try:
    df['AccountTypeID'] = df['AccountTypeID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['AccountTypeID'] = "not found"

try:
    df['AccountSubTypeID'] = df['AccountSubTypeID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['AccountSubTypeID'] = "not found"

try:
    df['LastUpgradeDate'] = df['LastUpgradeDate'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['LastUpgradeDate'] = "not found"

try:
    df['ActivatingStoreID'] = df['ActivatingStoreID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ActivatingStoreID'] = "not found"

try:
    df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['MonthlyAccess'] = 0.0

try:
    df['OriginalTotalMRC'] = df['OriginalTotalMRC'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['OriginalTotalMRC'] = 0.0

try:
    df['OriginalLineMRC'] = df['OriginalLineMRC'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['OriginalLineMRC'] = 0.0

try:
    df['ContractTerm'] = df['ContractTerm'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['ContractTerm'] = 0.0

try:
    df['KeyID'] = df['KeyID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['KeyID'] = "not found"

try:
    df['Coop'] = df['Coop'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['Coop'] = 0.0

try:
    df['Spiff'] = df['Spiff'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['Spiff'] = 0.0

try:
    df['Commission'] = df['Commission'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['Commission'] = 0.0

try:
    df['Deposit'] = df['Deposit'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['Deposit'] = 0.0

try:
    df['OrderID'] = df['OrderID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['OrderID'] = "not found"

try:
    df["ActDate"] = pd.to_datetime(df["ActDate"].fillna(0))
except:
    df['ActDate'] = 0

try:
    df["DeactDate"] = pd.to_datetime(df["DeactDate"].fillna(0))
except:
    df['DeactDate'] = 0

try:
    df["ReactDate"] = pd.to_datetime(df["ReactDate"].fillna(0))
except:
    df['ReactDate'] = 0

try:
    df['SIM'] = df['SIM'].fillna(0).astype(np.int64)
    df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIM'] = 0



## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-STATEMENT] ([ServiceUniversalID], [DealerCode], [DealerName], [MonthlyAccess], [PlanCode], [MarketCode], [ProductType], [ActivityType], [ActDate], [DeactDate], [ReactDate], [LineOfServiceID], [ServiceNumber], [CustomerName], [SIM], [IMEI], [BAN], [ContractTerm], [CreditType], [PreToPostMigration], [CreditClass], [HandSetOfferTypeIndicator], [SubdealerID], [ProdCatDescription], [ContractID], [MasterDealerCode], [Month], [CheckNumber], [IsEligible], [NonCommissionableReason], [Source], [AccountTypeID], [AccountSubTypeID], [LastUpgradeDate], [OriginalLineMRC], [OriginalTotalMRC], [ActivatingStoreID], [KeyID], [Coop], [Spiff], [Commission], [Deposit], [OrderID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['ServiceUniversalID'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['ReactDate'], row['LineOfServiceID'], row['ServiceNumber'], row['CustomerName'], row['SIM'], row['IMEI'], row['BAN'], row['ContractTerm'], row['CreditType'], row['PreToPostMigration'], row['CreditClass'], row['HandSetOfferTypeIndicator'], row['SubdealerID'], row['ProdCatDescription'], row['ContractID'], row['MasterDealerCode'], row['Month'], row['CheckNumber'], row['IsEligible'], row['NonCommissionableReason'], row['Source'], row['AccountTypeID'], row['AccountSubTypeID'], row['LastUpgradeDate'], row['OriginalLineMRC'], row['OriginalTotalMRC'], row['ActivatingStoreID'], row['KeyID'], row['Coop'], row['Spiff'], row['Commission'], row['Deposit'], row['OrderID'])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-STATEMENT] ([LineOfServiceID]) VALUES(?)", row["LineOfServiceID"])
cnxn.commit()
cursor.close()
print("done")

