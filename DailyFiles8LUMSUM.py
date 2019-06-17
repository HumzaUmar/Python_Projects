import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily LumSum\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily LumSum\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily LumSum\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily LumSum\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily LumSum\export\Master.xlsx', index=False))


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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily LumSum\export\Master.xlsx")

##############################################################################################################################
############ Datatypes
##############################################################################################################################

try:
    df['BatchID'] = df['BatchID'].astype(str).replace('\.0', '', regex=True)
except:
    df['BatchID'] = "not found"

try:
    df['LineItem'] = df['LineItem'].astype(str).replace('\.0', '', regex=True)
except:
    df['LineItem'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['PayoutType'] = df['PayoutType'].astype(str).replace('\.0', '', regex=True)
except:
    df['PayoutType'] = "not found"

try:
    df['PlanCode'] = df['PlanCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['PlanCode'] = "not found"

try:
    df['Month'] = df['Month'].astype(str).replace('\.0', '', regex=True)
except:
    df['Month'] = "not found"

try:
    df['Event'] = df['Event'].astype(str).replace('\.0', '', regex=True)
except:
    df['Event'] = "not found"

try:
    df['EventType'] = df['EventType'].astype(str).replace('\.0', '', regex=True)
except:
    df['EventType'] = "not found"

try:
    df['DealerVisibileComments'] = df['DealerVisibileComments'].astype(str).replace('\.0', '', regex=True)
except:
    df['DealerVisibileComments'] = "not found"

try:
    df['ContractID'] = df['ContractID'].astype(str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

try:
    df['DealerCode'] = df['DealerCode'].astype(str).replace('\.0', '', regex=True)
except:
    df['DealerCode'] = "not found"

try:
    df['ServiceUniversalID'] = df['ServiceUniversalID'].astype(str).replace('\.0', '', regex=True)
except:
    df['ServiceUniversalID'] = "not found"

try:
    df['BAN'] = df['BAN'].astype(str).replace('\.0', '', regex=True)
except:
    df['BAN'] = "not found"

try:
    df['MSISDN'] = df['MSISDN'].astype(str).replace('\.0', '', regex=True)
except:
    df['MSISDN'] = "not found"

try:
    # df['SIM'] = df['SIM'].astype(str).replace('\.0', '', regex=True)
    df['SIM'] = df['SIM'].fillna(0).astype(np.int64)
    df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIM'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['Market'] = df['Market'].astype(str).replace('\.0', '', regex=True)
except:
    df['Market'] = "not found"

try:
    df['ContractTerm'] = df['ContractTerm'].astype(str).replace('\.0', '', regex=True)
except:
    df['ContractTerm'] = "not found"

try:
    df['SKU'] = df['SKU'].astype(str).replace('\.0', '', regex=True)
except:
    df['SKU'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['StoreID'] = df['StoreID'].astype(str).replace('\.0', '', regex=True)
except:
    df['StoreID'] = "not found"

try:
    df['DollarAmount'] = df['DollarAmount'].fillna(0).astype(np.int).replace('\.0', '', regex=True)
except:
    df['DollarAmount'] = 0

try:
    df['MRC'] = df['MRC'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
except:
    df['MRC'] = 0.0


##############################################################################################################################
############ Database
##############################################################################################################################
# df.replace([np.nan], [""], inplace=True)

### DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-LUMSUM] ([BatchID],[LineItem],[MasterDealerCode],[PayoutType],[Month],[Event],[EventType],[DollarAmount],[DealerVisibileComments],[ContractID], [DealerCode], [ServiceUniversalID], [BAN], [MSISDN], [SIM], [IMEI], [Market], [MRC], [ContractTerm], [SKU], [CheckNumber], [StoreID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['BatchID'], row['LineItem'], row['MasterDealerCode'], row['PayoutType'], row['Month'], row['Event'], row['EventType'], row['DollarAmount'], row['DealerVisibileComments'], row['ContractID'], row['DealerCode'], row['ServiceUniversalID'], row['BAN'], row['MSISDN'], row['SIM'], row['IMEI'], row['Market'], row['MRC'], row['ContractTerm'], row['SKU'], row['CheckNumber'], row['StoreID'])
cnxn.commit()
cursor.close()
print("done")
