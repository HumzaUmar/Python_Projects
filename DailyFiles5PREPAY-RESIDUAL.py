import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
# ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Prepay Residual\{}".format(filename)
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily Prepay Residual\daily/'

files_xls = [f for f in files if f[-3:] == 'csv']

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_csv(path_file+f, delimiter="|", low_memory=False)
    df = df.append(data, sort=True)

print(df.to_excel(r'C:\xampp\htdocs\Terminal\Daily Prepay Residual\export\Master.xlsx', index=False))



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

df = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily Prepay Residual\export\Master.xlsx")

##############################################################################################################################
############ Datatypes
##############################################################################################################################

try:
    df['SERVICEUNIVERSALID'] = df['SERVICEUNIVERSALID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SERVICEUNIVERSALID'] = "not found"

try:
    df['SalesCode'] = df['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SalesCode'] = "not found"

try:
    df['DealerName'] = df['DealerName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['DealerName'] = "not found"

try:
    df['LineOfServiceID'] = df['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['LineOfServiceID'] = "not found"

try:
    df['CUSTOMERNAME'] = df['CUSTOMERNAME'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CUSTOMERNAME'] = "not found"

try:
    df['ServiceNumber'] = df['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ServiceNumber'] = "not found"

try:
    df['MARKETCODE'] = df['MARKETCODE'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MARKETCODE'] = "not found"

try:
    df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['MasterDealerCode'] = "not found"

try:
    df['BillingPlan'] = df['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['BillingPlan'] = "not found"

try:
    df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ContractID'] = "not found"

try:
    df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['CheckNumber'] = "not found"

try:
    df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SubDealerID'] = "not found"

try:
    df['ResidualType'] = df['ResidualType'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['ResidualType'] = "not found"

try:
    df['Month'] = df['Month'].astype(np.str).replace('\.0', '', regex=True)
    df["Month"] = pd.to_datetime(df["Month"].fillna(0))
except:
    df['Month'] = 0

try:
    df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['SIM'] = "not found"

try:
    df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['IMEI'] = "not found"

try:
    df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['MonthlyAccess'] = 0.0

try:
    df['ResidualPercent'] = df['ResidualPercent'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['ResidualPercent'] = 0.0

try:
    df['MonthsSinceLastActivation'] = df['MonthsSinceLastActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['MonthsSinceLastActivation'] = 0.0

try:
    df["BEGSERVDATE"] = pd.to_datetime(df["BEGSERVDATE"].fillna(0))
except:
    df['BEGSERVDATE'] = 0

try:
    df['DealerName'] = df['DealerName'].astype(np.str).replace('\.0', '', regex=True)
except:
    df['DealerName'] = "not found"

try:
    df["DateString"] = pd.to_datetime(df["DateString"].fillna(0))
except:
    df['DateString'] = 0

try:
    df['TotalResidual'] = df['TotalResidual'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
except:
    df['TotalResidual'] = 0.0

try:
    df['ProductCatDescription'] = df['ProductCatDescription'].astype(np.str)
except:
    df['ProductCatDescription'] = "not found"

try:
    df["SubBaseStartDate"] = pd.to_datetime(df["SubBaseStartDate"].fillna(0))
except:
    df['SubBaseStartDate'] = 0


##############################################################################################################################
############ Database
##############################################################################################################################

# cursor = cnxn.cursor()
# for index,row in df.iterrows():
#     cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PREPAY-RESIDUAL] ([SERVICEUNIVERSALID], [SalesCode], [CUSTOMERNAME], [BEGSERVDATE], [LineOfServiceID], [ServiceNumber], [MARKETCODE], [BillingPlan], [MonthlyAccess], [ResidualPercent], [ContractID], [SubDealerID], [ResidualType], [MonthsSinceLastActivation], [MasterDealerCode], [CheckNumber], [Month], [SIM],[IMEI]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     , row['SERVICEUNIVERSALID'], row['SalesCode'], row['CUSTOMERNAME'], row['BEGSERVDATE'], row['LineOfServiceID'], row['ServiceNumber'], row['MARKETCODE'], row['BillingPlan'], row['MonthlyAccess'], row['ResidualPercent'], row['ContractID'], row['SubDealerID'], row['ResidualType'], row['MonthsSinceLastActivation'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'])
#
#     # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PREPAY-RESIDUAL] ([ContractID]) VALUES(?)", row["ContractID"])
# cnxn.commit()
# cursor.close()
# print("done")


## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PREPAY-RESIDUAL] ([SERVICEUNIVERSALID], [SalesCode], [CUSTOMERNAME], [BEGSERVDATE], [LineOfServiceID], [ServiceNumber], [MARKETCODE], [BillingPlan], [MonthlyAccess], [ResidualPercent], [ContractID], [SubDealerID], [ResidualType], [MonthsSinceLastActivation], [MasterDealerCode], [CheckNumber], [Month], [SIM],[IMEI],[DealerName],[DateString],[TotalResidual],[ProductCatDescription],[SubBaseStartDate]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['SERVICEUNIVERSALID'], row['SalesCode'], row['CUSTOMERNAME'], row['BEGSERVDATE'], row['LineOfServiceID'], row['ServiceNumber'], row['MARKETCODE'], row['BillingPlan'], row['MonthlyAccess'], row['ResidualPercent'], row['ContractID'], row['SubDealerID'], row['ResidualType'], row['MonthsSinceLastActivation'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'], row['DealerName'],row['DateString'],row['TotalResidual'],row['ProductCatDescription'],row['SubBaseStartDate'])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PREPAY-RESIDUAL] ([ContractID]) VALUES(?)", row["ContractID"])
cnxn.commit()
cursor.close()
print("done")
