import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Prepaid Residual\export\Master.xlsx', index=False))


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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Prepaid Residual\export\Master.xlsx", delimiter="|")

##############################################################################################################################
############ Datatypes
##############################################################################################################################

# df['SalesCode'] = df['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
# df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
# df['SubscriberID'] = df['SubscriberID'].astype(np.str).replace('\.0', '', regex=True)
# df['ServiceNo'] = df['ServiceNo'].astype(np.str).replace('\.0', '', regex=True)
# df['RatePlanCode'] = df['RatePlanCode'].astype(np.str).replace('\.0', '', regex=True)
# df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
# df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
# df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
# df['FirstName'] = df['FirstName'].astype(np.str).replace('\.0', '', regex=True)
# df['LastName'] = df['LastName'].astype(np.str).replace('\.0', '', regex=True)
#
# df['RefillAmt'] = df['RefillAmt'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
# df['DaysSinceActivation'] = df['DaysSinceActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
#
# df["RefillDate"] = pd.to_datetime(df["RefillDate"])
# df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
# df["Month"] = pd.to_datetime(df["Month"].fillna(0))


try:
    df['SalesCode'] = df['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SalesCode'] = "not found"

try:
    df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

try:
    df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SubDealerID'] = "not found"

try:
    df['SubscriberID'] = df['SubscriberID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SubscriberID'] = "not found"

try:
    df['ServiceNo'] = df['ServiceNo'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ServiceNo'] = "not found"

try:
    df['RatePlanCode'] = df['RatePlanCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['RatePlanCode'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIM'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['FirstName'] = df['FirstName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['FirstName'] = "not found"

try:
    df['LastName'] = df['LastName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['LastName'] = "not found"

try:
    df['RefillAmt'] = df['RefillAmt'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['RefillAmt'] = 0.0

try:
    df['DaysSinceActivation'] = df['DaysSinceActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['DaysSinceActivation'] = 0.0

try:
    df["RefillDate"] = pd.to_datetime(df["RefillDate"].fillna(0))
except:
    df['RefillDate'] = 0

try:
    df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
    df["Month"] = pd.to_datetime(df["Month"].fillna(0))
except:
    df['Month'] = 0

try:
    df['FillAmount'] = df['FillAmount'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['FillAmount'] = 0.0

try:
    df['TotalResidual'] = df['TotalResidual'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['TotalResidual'] = 0.0


try:
    df['ResidualPCT'] = df['ResidualPCT'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['ResidualPCT'] = 0.0


try:
    df["BeginServiceDate"] = pd.to_datetime(df["BeginServiceDate"].fillna(0))
except:
    df["BeginServiceDate"] = 0

try:
    df['BillingPlan'] = df['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['BillingPlan'] = "not found"

try:
    df['ProductCatDescription'] = df['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProductCatDescription'] = "not found"

try:
    df['ProductCatDescription'] = df['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ProductCatDescription'] = "not found"

try:
    df['DealerCode'] = df['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['DealerCode'] = "not found"

try:
    df['TransactionID'] = df['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['TransactionID'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['DealerName'] = df['DealerName'].astype(np.str)
except:
    df['DealerName'] = "not found"

##############################################################################################################################
############ Database
##############################################################################################################################

# ## DATABASE
# cursor = cnxn.cursor()
# for index,row in df.iterrows():
#     cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([SalesCode], [ContractID], [SubDealerID], [SubscriberID], [FirstName], [LastName], [RefillDate], [ServiceNo], [MarketCode], [RatePlanCode], [RefillAmt], [DaysSinceActivation], [DealerName], [MasterDealerCode], [CheckNumber], [Month], [SIM], [IMEI]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     , row['SalesCode'], row['ContractID'], row['SubDealerID'], row['SubscriberID'], row['FirstName'], row['LastName'], row['RefillDate'], row['ServiceNo'], row['MarketCode'], row['RatePlanCode'], row['RefillAmt'], row['DaysSinceActivation'], row['DealerName'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'])
#
#     # cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([IMEI]) VALUES(?)", row["IMEI"])
# cnxn.commit()
# cursor.close()
# print("done")


cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([SalesCode], [ContractID], [SubDealerID], [SubscriberID], [FirstName], [LastName], [RefillDate], [ServiceNo], [MarketCode], [RatePlanCode], [RefillAmt], [DaysSinceActivation], [DealerName], [MasterDealerCode], [CheckNumber], [Month], [SIM], [IMEI], [FillAmount], [TotalResidual], [ResidualPCT], [BeginServiceDate], [BillingPlan], [ProductCatDescription], [DealerCode], [TransactionID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['SalesCode'], row['ContractID'], row['SubDealerID'], row['SubscriberID'], row['FirstName'], row['LastName'], row['RefillDate'], row['ServiceNo'], row['MarketCode'], row['RatePlanCode'], row['RefillAmt'], row['DaysSinceActivation'], row['DealerName'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'], row["FillAmount"], row["TotalResidual"], row["ResidualPCT"], row["BeginServiceDate"], row["BillingPlan"], row["ProductCatDescription"], row["DealerCode"], row["TransactionID"])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([IMEI]) VALUES(?)", row["IMEI"])
cnxn.commit()
cursor.close()
print("done")

##############################################################################################################################
############################################################################################################################