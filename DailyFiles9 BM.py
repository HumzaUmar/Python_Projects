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

df = pd.read_csv(r"C:\Users\RD1\Desktop\New folder (3)\DAILY\DAILY-BM-3462409__2019 04 (APR)__04193462409ALL20190421145116.csv", delimiter="|", low_memory=False)

print(df.shape)
df['CCID'] = df['CCID'].astype(np.str).replace('\.0', '', regex=True)
df['EffectiveCalcDate'] = df['EffectiveCalcDate'].astype(np.str).replace('\.0', '', regex=True)
df['BAN'] = df['BAN'].astype(np.str).replace('\.0', '', regex=True)
df['BankID'] = df['BankID'].astype(np.str).replace('\.0', '', regex=True)
df['Event'] = df['Event'].astype(np.str).replace('\.0', '', regex=True)
df['EventType'] = df['EventType'].astype(np.str).replace('\.0', '', regex=True)
df['SpiffID'] = df['SpiffID'].astype(np.str).replace('\.0', '', regex=True)
df['DealerCode'] = df['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
df['DealerName'] = df['DealerName'].astype(np.str).replace('\.0', '', regex=True)
df['MasterDealerCode'] = df['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
df['CheckNumber'] = df['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
df['SubDealerID'] = df['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
df['ContractID'] = df['ContractID'].astype(np.str).replace('\.0', '', regex=True)

df['Value'] = df['Value'].fillna(0).astype(np.float).replace('\.0', '', regex=True)

default ="2010-10-01"
df["EffectiveCalcDate"] = pd.to_datetime(df["EffectiveCalcDate"].fillna(default))

df['Month'] = df['Month'].str.replace("(" ,"").str.replace(")","")
df["Month"] = pd.to_datetime(df["Month"].fillna(default))


## DATABASE
cursor = cnxn.cursor()
for index,row in df.iterrows():
    cursor.execute("INSERT INTO [Test].[dbo].[DAILY-BM] ([CCID], [EffectiveCalcDate], [BAN], [BankID], [Event], [EventType], [SpiffID], [DealerCode], [DealerName], [Month], [Value], [MasterDealerCode], [CheckNumber], [SubDealerID], [ContractID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    , row['CCID'], row['EffectiveCalcDate'], row['BAN'], row['BankID'], row['Event'], row['EventType'], row['SpiffID'], row['DealerCode'], row['DealerName'], row['Month'], row['Value'], row['MasterDealerCode'], row['CheckNumber'], row['SubDealerID'], row['ContractID'])

    # cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([IMEI]) VALUES(?)", row["IMEI"])
cnxn.commit()
cursor.close()
print("done")