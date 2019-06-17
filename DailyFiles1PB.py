import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily PB\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
# ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily PB\{}".format(filename)
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily PB\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily PB\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily PB/daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily PB\export\Master.xlsx', index=False))


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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily PB\export\Master.xlsx")

#######################

# df['ServiceUniversalID'] = df['ServiceUniversalID'].astype(str).replace('\.0', '', regex=True)
# df['DealerCode'] = df['DealerCode'].astype(str).replace('\.0', '', regex=True)
# df['DealerName'] = df['DealerName'].astype(str).replace('\.0', '', regex=True)
# df['IMEI'] = df['IMEI'].astype(str).replace('\.0', '', regex=True)
# df['PlanCode'] = df['PlanCode'].astype(str).replace('\.0', '', regex=True)
# df['MarketCode'] = df['MarketCode'].astype(str).replace('\.0', '', regex=True)
# df['ProductType'] = df['ProductType'].astype(str).replace('\.0', '', regex=True)
# df['ActivityType'] = df['ActivityType'].astype(str).replace('\.0', '', regex=True)
# df['ServiceNumber'] = df['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
# df['CustomerName'] = df['CustomerName'].astype(str).replace('\.0', '', regex=True)
# df['InvoiceNumber'] = df['InvoiceNumber'].astype(str).replace('\.0', '', regex=True)
# df['BAN'] = df['BAN'].astype(str).replace('\.0', '', regex=True)
# df['DealerCode'] = df['DealerCode'].astype(str).replace('\.0', '', regex=True)
# df['ServiceNumber'] = df['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
# df['IMEI'] = df['IMEI'].astype(str).replace('\.0', '', regex=True)
# df['BAN'] = df['BAN'].astype(str).replace('\.0', '', regex=True)
# df['SubDealerID'] = df['SubDealerID'].astype(str).replace('\.0', '', regex=True)
# df['ActivatingStoreID'] = df['ActivatingStoreID'].astype(str).replace('\.0', '', regex=True)
# df['ContractID'] = df['ContractID'].astype(str).replace('\.0', '', regex=True)
# df['MasterDealerCode'] = df['MasterDealerCode'].astype(str).replace('\.0', '', regex=True)
# df['CheckNumber'] = df['CheckNumber'].astype(str).replace('\.0', '', regex=True)
# df['PerformanceBonusType'] = df['PerformanceBonusType'].astype(str).replace('\.0', '', regex=True)
# df['PerformanceBonusName'] = df['PerformanceBonusName'].astype(str).replace('\.0', '', regex=True)
# df['ProductDescription'] = df['ProductDescription'].astype(str).replace('\.0', '', regex=True)
# df['PerformanceBonus2Category'] = df['PerformanceBonus2Category'].astype(str).replace('\.0', '', regex=True)
#
# df['Qty'] = df['Qty'].fillna(0).astype(np.int).replace('\.0', '', regex=True)
# df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
# df['CustomerPaidAmount'] = df['CustomerPaidAmount'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
# df['NUM'] = df['NUM'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
# df['DEN'] = df['DEN'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
#
# df['SIM'] = df['SIM'].fillna(0).astype(np.int64)
# df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
# df.replace([np.nan], [""], inplace=True)

##############################################################################################################################
############ Datatypes
##############################################################################################################################

try:
    df['ServiceUniversalID'] = df['ServiceUniversalID'].astype(str).replace('\.0', '', regex=True)
except:
    df['ServiceUniversalID'] = "not found"

try:
    df['DealerCode'] = df['DealerCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['DealerCode'] = "not found"

try:
    df['DealerName'] = df['DealerName'].astype(str).replace('\.0', '', regex=True)
except:
    df['DealerName'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['PlanCode'] = df['PlanCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['PlanCode'] = "not found"

try:
    df['MarketCode'] = df['MarketCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['MarketCode'] = "not found"

try:
    df['ProductType'] = df['ProductType'].astype(str).replace('\.0', '', regex=True)
except:
    df['ProductType'] = "not found"

try:
    df['ActivityType'] = df['ActivityType'].astype(str).replace('\.0', '', regex=True)
except:
    df['ActivityType'] = "not found"

try:
    df['ServiceNumber'] = df['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
except:
    df['ServiceNumber'] = "not found"

try:
    df['CustomerName'] = df['CustomerName'].astype(str).replace('\.0', '', regex=True)
except:
    df['CustomerName'] = "not found"

try:
    df['InvoiceNumber'] = df['InvoiceNumber'].astype(str).replace('\.0', '', regex=True)
except:
    df['InvoiceNumber'] = "not found"

try:
    df['BAN'] = df['BAN'].astype(str).replace('\.0', '', regex=True)
except:
    df['BAN'] = "not found"

try:
    df['DealerCode'] = df['DealerCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['DealerCode'] = "not found"

try:
    df['ServiceNumber'] = df['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
except:
    df['ServiceNumber'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['BAN'] = df['BAN'].astype(str).replace('\.0', '', regex=True)
except:
    df['BAN'] = "not found"

try:
    df['SubDealerID'] = df['SubDealerID'].astype(str).replace('\.0', '', regex=True)
except:
    df['SubDealerID'] = "not found"

try:
    df['ActivatingStoreID'] = df['ActivatingStoreID'].astype(str).replace('\.0', '', regex=True)
except:
    df['ActivatingStoreID'] = "not found"

try:
    df['ContractID'] = df['ContractID'].astype(str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['PerformanceBonusType'] = df['PerformanceBonusType'].astype(str).replace('\.0', '', regex=True)
except:
    df['PerformanceBonusType'] = "not found"

try:
    df['PerformanceBonusName'] = df['PerformanceBonusName'].astype(str).replace('\.0', '', regex=True)
except:
    df['PerformanceBonusName'] = "not found"

try:
    df['ProductDescription'] = df['ProductDescription'].astype(str).replace('\.0', '', regex=True)
except:
    df['ProductDescription'] = "not found"

try:
    df['PerformanceBonus2Category'] = df['PerformanceBonus2Category'].astype(str).replace('\.0', '', regex=True)
except:
    df['PerformanceBonus2Category'] = "not found"

try:
    df['Qty'] = df['Qty'].fillna(0).astype(np.int).replace('\.0', '', regex=True)
except:
    df['Qty'] = 0

try:
    df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['MonthlyAccess'] = 0.0

try:
    df['CustomerPaidAmount'] = df['CustomerPaidAmount'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['CustomerPaidAmount'] = 0.0

try:
    df['NUM'] = df['NUM'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['NUM'] = 0.0

try:
    df['DEN'] = df['DEN'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['DEN'] = 0.0

try:
    df['SIM'] = df['SIM'].fillna(0).astype(np.int64)
    df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIM'] = 0

##############################################################################################################################
############ Database
##############################################################################################################################
df.replace([np.nan], [""], inplace=True)


### DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PB] ([ServiceUniversalID],[DealerCode],[DealerName],[MonthlyAccess],[PlanCode],[MarketCode],[ProductType],[ActivityType],[ActDate],[DeactDate], [ReactDate], [ServiceNumber], [CustomerName], [InvoiceNumber], [SIM], [IMEI], [BAN], [CustomerPaidAmount], [Qty], [SubDealerID], [ActivatingStoreID], [ContractID], [Month], [MasterDealerCode], [CheckNumber], [PerformanceBonusType], [PerformanceBonusName], [NUM], [DEN], [ProductDescription], [EffectiveCalcDate], [PerformanceBonus2Category]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['ServiceUniversalID'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['ReactDate'], row['ServiceNumber'], row['CustomerName'], row['InvoiceNumber'], row['SIM'], row['IMEI'], row['BAN'], row['CustomerPaidAmount'], row['Qty'], row['SubDealerID'], row['ActivatingStoreID'], row['ContractID'], row['Month'], row['MasterDealerCode'], row['CheckNumber'], row['PerformanceBonusType'], row['PerformanceBonusName'], row['NUM'], row['DEN'], row['ProductDescription'], str(row['EffectiveCalcDate']), row['PerformanceBonus2Category'])
cnxn.commit()
cursor.close()
print("done")
