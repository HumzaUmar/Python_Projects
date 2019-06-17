import numpy as np
import re
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

df = pd.read_csv(r"C:\Users\RD1\Desktop\New folder (3)\DAILY\DAILY-RESIDUAL-3462409__2019 04 (APR)__04193462409ALL20190421153312.csv", delimiter="|", low_memory=False)



df['SERVICEUNIVERSALID'] = df['SERVICEUNIVERSALID'].astype(np.str).replace('\.0', '', regex=True)
df['SalesCode'] = df['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
df['CUSTOMERNAME'] = df['CUSTOMERNAME'].astype(np.str).replace('\.0', '', regex=True)
df['FAN'] = df['FAN'].astype(np.str).replace('\.0', '', regex=True)
df['LineOfServiceID'] = df['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
df['ServiceNumber'] = df['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
df['MARKETCODE'] = df['MARKETCODE'].astype(np.str).replace('\.0', '', regex=True)
df['BillingPlan'] = df['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)
df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
df['ResidualType'] = df['ResidualType'].astype(np.str).replace('\.0', '', regex=True)
df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
# df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)
df['IMEI'] = df['IMEI'].astype(np.str).replace('\.0', '', regex=True)

df['MonthlyAccess'] = df['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
df['ResidualPercent'] = df['ResidualPercent'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
df['MonthsSinceLastActivation'] = df['MonthsSinceLastActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)

default ="2010-10-01"
df["BEGSERVDATE"] = pd.to_datetime(df["BEGSERVDATE"].fillna(default))

df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
df["Month"] = pd.to_datetime(df["Month"].fillna(default))

df['SIM'] = df['SIM'].fillna(0).astype(np.int64)
df['SIM'] = df['SIM'].astype(np.str).replace('\.0', '', regex=True)


# 8901260932785990000
# 8901260381799180000

## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-RESIDUAL] ([SERVICEUNIVERSALID], [SalesCode], [CUSTOMERNAME], [FAN], [BEGSERVDATE], [LineOfServiceID], [ServiceNumber], [MARKETCODE], [BillingPlan], [MonthlyAccess], [ResidualPercent], [ContractID], [SubDealerID], [ResidualType], [MonthsSinceLastActivation], [MasterDealerCode], [CheckNumber], [Month], [SIM], [IMEI]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['SERVICEUNIVERSALID'], row['SalesCode'], row['CUSTOMERNAME'], row['FAN'], row['BEGSERVDATE'], row['LineOfServiceID'], row['ServiceNumber'], row['MARKETCODE'], row['BillingPlan'],  row['MonthlyAccess'], row['ResidualPercent'], row['ContractID'], row['SubDealerID'], row['ResidualType'], row['MonthsSinceLastActivation'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-SPIFF] ([LastSuspendDate]) VALUES(?)", row["LastSuspendDate"])
cnxn.commit()
cursor.close()
print("done")
