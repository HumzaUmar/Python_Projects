import pandas as pd
import os
import zipfile
import glob

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

##### LINKS
dirzip = glob.glob(r"C:\xampp\htdocs\Terminal\Daily All Details\daily/*.zip")
filename = dirzip[0]
filename = os.path.basename(filename).split(".")[0]
ziptopdffolder = r"C:\xampp\htdocs\Terminal\Daily All Details\daily"

##### EXTRACTIONS
zip_ref = zipfile.ZipFile(dirzip[0], 'r')
zip_ref.extractall(ziptopdffolder)
zip_ref.close()

path = os.getcwd()
files = os.listdir(r'C:\xampp\htdocs\Terminal\Daily All Details\daily')
path_file = r'C:\xampp\htdocs\Terminal\Daily All Details\daily/'

files_xls = [f for f in files if f[-4:] == 'xlsx']
fileslen = len(files_xls)

shts =['HANDSET',
     'SPIFF',
     'PREPAID-RESIDUAL',
     'ACCESSORY',
     'LUMP-SUM',
     'RESIDUAL',
     'STATEMENT',
     'PREPAY-RESIDUAL',
     'PB']


# for s in shts:
#     # frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\daily\ALL-DETAILS-03193462409ALL20190421061540.xlsx", sheet_name=s)
#     frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\daily\{}".format(files_xls[0]),sheet_name=s)
#     print(frame.to_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\{}.xlsx".format(s), index=False))

for s in shts:
    for i in range(fileslen):
        # frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\daily\ALL-DETAILS-03193462409ALL20190421061540.xlsx", sheet_name=s)
        frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\daily\{}".format(files_xls[i]),sheet_name=s)
        print(frame.to_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\{}.xlsx".format(s), index=False))


import pyodbc
import pandas as pd
import warnings
import numpy as np

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)
pd.options.display.max_colwidth = 200

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RD1\RD1;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

##### WARNINGS
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# shts =['HANDSET',
#      'SPIFF',
#      'PREPAID-RESIDUAL',
#      'ACCESSORY',
#      'LUMP-SUM',
#      'RESIDUAL',
#      'STATEMENT',
#      'PREPAY-RESIDUAL',
#      'PB']
#
# for s in shts:
#         # frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\daily\ALL-DETAILS-03193462409ALL20190421061540.xlsx", sheet_name=s)
#         frame = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\export\Master.xlsx",sheet_name=s)
#         print(frame.to_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\{}.xlsx".format(s), index=False))

try:
    lumsum = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\LUMP-SUM.xlsx")

    try:
        lumsum['BatchID'] = lumsum['BatchID'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['BatchID'] = "not found"

    try:
        lumsum['LineItem'] = lumsum['LineItem'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['LineItem'] = "not found"

    try:
        lumsum['MasterDealerCode'] = lumsum['MasterDealerCode'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['MasterDealerCode'] = "not found"

    try:
        lumsum['PayoutType'] = lumsum['PayoutType'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['PayoutType'] = "not found"

    try:
        lumsum['PlanCode'] = lumsum['PlanCode'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['PlanCode'] = "not found"

    try:
        lumsum['Month'] = lumsum['Month'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['Month'] = "not found"

    try:
        lumsum['Event'] = lumsum['Event'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['Event'] = "not found"

    try:
        lumsum['EventType'] = lumsum['EventType'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['EventType'] = "not found"

    try:
        lumsum['DealerVisibileComments'] = lumsum['DealerVisibileComments'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['DealerVisibileComments'] = "not found"

    try:
        lumsum['ContractID'] = lumsum['ContractID'].astype(str).replace('\.0', 'nan', regex=True)
    except:
        lumsum['ContractID'] = "not found"

    try:
        lumsum['DealerCode'] = lumsum['DealerCode'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['DealerCode'] = "not found"

    try:
        lumsum['ServiceUniversalID'] = lumsum['ServiceUniversalID'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['ServiceUniversalID'] = "not found"

    try:
        lumsum['BAN'] = lumsum['BAN'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['BAN'] = "not found"

    try:
        lumsum['MSISDN'] = lumsum['MSISDN'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['MSISDN'] = "not found"

    try:
        lumsum['SIM'] = lumsum['SIM'].fillna(0).astype(np.int64)
        lumsum['SIM'] = lumsum['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        lumsum['SIM'] = "not found"

    try:
        lumsum['IMEI'] = lumsum['IMEI'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['IMEI'] = "not found"

    try:
        lumsum['Market'] = lumsum['Market'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['Market'] = "not found"

    try:
        lumsum['ContractTerm'] = lumsum['ContractTerm'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['ContractTerm'] = "not found"

    try:
        lumsum['SKU'] = lumsum['SKU'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['SKU'] = "not found"

    try:
        lumsum['CheckNumber'] = lumsum['CheckNumber'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['CheckNumber'] = "not found"

    try:
        lumsum['StoreID'] = lumsum['StoreID'].astype(str).replace('\.0', '', regex=True)
    except:
        lumsum['StoreID'] = "not found"

    try:
        lumsum['DollarAmount'] = lumsum['DollarAmount'].fillna(0).astype(np.int).replace('\.0', '', regex=True)
    except:
        lumsum['DollarAmount'] = 0

    try:
        lumsum['MRC'] = lumsum['MRC'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        lumsum['MRC'] = 0.0

    # print(lumsum)
    # statement.replace([np.nan], [""], inplace=True)

    ##############################################################################################################################
    ############ Database
    ##############################################################################################################################


    ### DATABASE
    cursor = cnxn.cursor()
    for index,row in lumsum.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-LUMSUM] ([BatchID],[LineItem],[MasterDealerCode],[PayoutType],[Month],[Event],[EventType],[DollarAmount],[DealerVisibileComments],[ContractID], [DealerCode], [ServiceUniversalID], [BAN], [MSISDN], [SIM], [IMEI], [Market], [MRC], [ContractTerm], [SKU], [CheckNumber], [StoreID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['BatchID'], row['LineItem'], row['MasterDealerCode'], row['PayoutType'], row['Month'], row['Event'], row['EventType'], row['DollarAmount'], row['DealerVisibileComments'], row['ContractID'], row['DealerCode'], row['ServiceUniversalID'], row['BAN'], row['MSISDN'], row['SIM'], row['IMEI'], row['Market'], row['MRC'], row['ContractTerm'], row['SKU'], row['CheckNumber'], row['StoreID'])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


####################################################################################################
####################################################################################################

try:
    statement = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\STATEMENT.xlsx")

    try:
        statement['ServiceUniversalID'] = statement['ServiceUniversalID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ServiceUniversalID'] = "not found"

    try:
        statement['DealerCode'] = statement['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['DealerCode'] = "not found"

    try:
        statement['DealerName'] = statement['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['DealerName'] = "not found"

    try:
        statement['PlanCode'] = statement['PlanCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['PlanCode'] = "not found"

    try:
        statement['DealerName'] = statement['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['DealerName'] = "not found"

    try:
        statement['PlanCode'] = statement['PlanCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['PlanCode'] = "not found"

    try:
        statement['MarketCode'] = statement['MarketCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['MarketCode'] = "not found"

    try:
        statement['ProductType'] = statement['ProductType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ProductType'] = "not found"

    try:
        statement['ActivityType'] = statement['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ActivityType'] = "not found"

    try:
        statement['LineOfServiceID'] = statement['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['LineOfServiceID'] = "not found"

    try:
        statement['ServiceNumber'] = statement['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ServiceNumber'] = "not found"

    try:
        statement['CustomerName'] = statement['CustomerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['CustomerName'] = "not found"

    try:
        statement['IMEI'] = statement['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['IMEI'] = "not found"

    try:
        statement['BAN'] = statement['BAN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['BAN'] = "not found"

    try:
        statement['CreditType'] = statement['CreditType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['CreditType'] = "not found"

    try:
        statement['PreToPostMigration'] = statement['PreToPostMigration'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['PreToPostMigration'] = "not found"

    try:
        statement['CreditClass'] = statement['CreditClass'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['CreditClass'] = "not found"

    try:
        statement['HandSetOfferTypeIndicator'] = statement['HandSetOfferTypeIndicator'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['HandSetOfferTypeIndicator'] = "not found"

    try:
        statement['SubdealerID'] = statement['SubdealerID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['SubdealerID'] = "not found"

    try:
        statement['ProdCatDescription'] = statement['ProdCatDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ProdCatDescription'] = "not found"

    try:
        statement['ContractID'] = statement['ContractID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ContractID'] = "not found"

    try:
        statement['MasterDealerCode'] = statement['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['MasterDealerCode'] = "not found"

    try:
        statement['Month'] = statement['Month'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['Month'] = "not found"

    try:
        statement['CheckNumber'] = statement['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['CheckNumber'] = "not found"

    try:
        statement['IsEligible'] = statement['IsEligible'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['IsEligible'] = "not found"

    try:
        statement['NonCommissionableReason'] = statement['NonCommissionableReason'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['NonCommissionableReason'] = "not found"

    try:
        statement['Source'] = statement['Source'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['Source'] = "not found"

    try:
        statement['AccountTypeID'] = statement['AccountTypeID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['AccountTypeID'] = "not found"

    try:
        statement['AccountSubTypeID'] = statement['AccountSubTypeID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['AccountSubTypeID'] = "not found"

    try:
        statement['LastUpgradeDate'] = statement['LastUpgradeDate'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['LastUpgradeDate'] = "not found"

    try:
        statement['ActivatingStoreID'] = statement['ActivatingStoreID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['ActivatingStoreID'] = "not found"

    try:
        statement['MonthlyAccess'] = statement['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['MonthlyAccess'] = 0.0

    try:
        statement['OriginalTotalMRC'] = statement['OriginalTotalMRC'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['OriginalTotalMRC'] = 0.0

    try:
        statement['OriginalLineMRC'] = statement['OriginalLineMRC'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['OriginalLineMRC'] = 0.0

    try:
        statement['ContractTerm'] = statement['ContractTerm'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['ContractTerm'] = 0.0

    try:
        statement['KeyID'] = statement['KeyID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['KeyID'] = "not found"

    try:
        statement['Coop'] = statement['Coop'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['Coop'] = 0.0

    try:
        statement['Spiff'] = statement['Spiff'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['Spiff'] = 0.0

    try:
        statement['Commission'] = statement['Commission'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['Commission'] = 0.0

    try:
        statement['Deposit'] = statement['Deposit'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        statement['Deposit'] = 0.0

    try:
        statement['OrderID'] = statement['OrderID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['OrderID'] = "not found"

    try:
        statement["ActDate"] = pd.to_datetime(statement["ActDate"].fillna(0))
    except:
        statement['ActDate'] = 0

    try:
        statement["DeactDate"] = pd.to_datetime(statement["DeactDate"].fillna(0))
    except:
        statement['DeactDate'] = 0

    try:
        statement["ReactDate"] = pd.to_datetime(statement["ReactDate"].fillna(0))
    except:
        statement['ReactDate'] = 0

    try:
        statement['SIM'] = statement['SIM'].fillna(0).astype(np.int64)
        statement['SIM'] = statement['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        statement['SIM'] = 0



    ## DATABASE
    cursor = cnxn.cursor()
    for index,row in statement.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-STATEMENT] ([ServiceUniversalID], [DealerCode], [DealerName], [MonthlyAccess], [PlanCode], [MarketCode], [ProductType], [ActivityType], [ActDate], [DeactDate], [ReactDate], [LineOfServiceID], [ServiceNumber], [CustomerName], [SIM], [IMEI], [BAN], [ContractTerm], [CreditType], [PreToPostMigration], [CreditClass], [HandSetOfferTypeIndicator], [SubdealerID], [ProdCatDescription], [ContractID], [MasterDealerCode], [Month], [CheckNumber], [IsEligible], [NonCommissionableReason], [Source], [AccountTypeID], [AccountSubTypeID], [LastUpgradeDate], [OriginalLineMRC], [OriginalTotalMRC], [ActivatingStoreID], [KeyID], [Coop], [Spiff], [Commission], [Deposit], [OrderID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['ServiceUniversalID'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['ReactDate'], row['LineOfServiceID'], row['ServiceNumber'], row['CustomerName'], row['SIM'], row['IMEI'], row['BAN'], row['ContractTerm'], row['CreditType'], row['PreToPostMigration'], row['CreditClass'], row['HandSetOfferTypeIndicator'], row['SubdealerID'], row['ProdCatDescription'], row['ContractID'], row['MasterDealerCode'], row['Month'], row['CheckNumber'], row['IsEligible'], row['NonCommissionableReason'], row['Source'], row['AccountTypeID'], row['AccountSubTypeID'], row['LastUpgradeDate'], row['OriginalLineMRC'], row['OriginalTotalMRC'], row['ActivatingStoreID'], row['KeyID'], row['Coop'], row['Spiff'], row['Commission'], row['Deposit'], row['OrderID'])

        # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-STATEMENT] ([LineOfServiceID]) VALUES(?)", row["LineOfServiceID"])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass

############################################################################################
############################################################################################

try:
    accessory = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\ACCESSORY.xlsx")

    try:
        accessory['SalesCode'] = accessory["SalesPersonCode"]
    except:
        accessory['SalesCode'] = "not found"

    try:
        accessory['TransactionID'] = accessory['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['TransactionID'] = "not found"

    try:
        accessory['InvoiceNumber'] = accessory['InvoiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['InvoiceNumber'] = "not found"

    try:
        accessory['CheckNumber'] = accessory['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['CheckNumber'] = "not found"

    try:
        accessory['BAN'] = accessory['BAN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['SalesCode'] = "not found"

    try:
        accessory['IMEI'] = accessory['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['IMEI'] = "not found"

    try:
        accessory['ActivityType'] = accessory['ActivityType'].astype(np.str)
    except:
        accessory['ActivityType'] = "not found"

    try:
        accessory['MSISDN'] = accessory['MSISDN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['MSISDN'] = "not found"

    try:
        accessory['OrderID'] = accessory['OrderID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['OrderID'] = "not found"

    try:
        accessory['MasterDealerCode'] = accessory['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['MasterDealerCode'] = "not found"

    try:
        accessory['SalesCode'] = accessory['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['SalesCode'] = "not found"

    try:
        accessory['LineOfServiceID'] = accessory['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['LineOfServiceID'] = "not found"

    try:
        accessory['Source'] = accessory['Source'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['Source'] = "not found"

    try:
        accessory['StoreID'] = accessory['StoreID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['StoreID'] = "not found"

    try:
        accessory['SAPTransTypeCode'] = accessory['SAPTransTypeCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['SAPTransTypeCode'] = "not found"

    try:
        accessory['ProxyID'] = accessory['ProxyID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        accessory['ProxyID'] = "not found"

    try:
        accessory['Month'] = accessory['Month'].str.replace("(" ,"").str.replace(")","")
        accessory["Month"] = pd.to_datetime(accessory["Month"].fillna(0))
    except:
        accessory['Month'] = 0

    try:
        accessory["TransactionDate"] = pd.to_datetime(accessory["TransactionDate"])
    except:
        accessory['TransactionDate'] = 0

    try:
        accessory['MSRP'] = accessory['MSRP'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        accessory['MSRP'] = 0

    try:
        accessory['SellingPrice'] = accessory['SellingPrice'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        accessory['SellingPrice'] = 0.0

    try:
        accessory['CustomerPaidAmt'] = accessory['CustomerPaidAmt'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        accessory['CustomerPaidAmt'] = 0.0

    try:
        accessory['CommissionAmount'] = accessory['CommissionAmount'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        accessory['CommissionAmount'] = 0.0

    try:
        accessory['QTY'] = accessory['QTY'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        accessory['QTY'] = 0.0


    ## DATABASE
    cursor = cnxn.cursor()
    for index,row in accessory.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-ACCESSORY] ([TransactionID], [MasterDealerCode], [CheckNumber], [Month], [SalesCode], [TransactionDate], [StoreID], [InvoiceNumber], [MSRP], [POSType], [ActivityType], [SellingPrice], [CustomerPaidAmt], [SKU], [IMEI], [LineOfServiceID], [BAN], [MSISDN], [SAPTransTypeCode], [ProductCategory], [ProductDescription], [QTY], [Source], [ProxyID], [OrderID],[CommissionAmount]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['TransactionID'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SalesCode'], row['TransactionDate'], row['StoreID'], row['InvoiceNumber'], row['MSRP'], row['POSType'], row['ActivityType'], row['SellingPrice'], row['CustomerPaidAmt'], row['SKU'], row['IMEI'], row['LineOfServiceID'], row['BAN'], row['MSISDN'], row['SAPTransTypeCode'], row['ProductCategory'], row['ProductDescription'], row['QTY'], row['Source'], row['ProxyID'], row['OrderID'], row['CommissionAmount'])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


############################################################################################
############################################################################################

try:
    prepaidresidual = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\PREPAID-RESIDUAL.xlsx")

    try:
        prepaidresidual['SalesCode'] = prepaidresidual['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['SalesCode'] = "not found"

    try:
        prepaidresidual['ContractID'] = prepaidresidual['ContractID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['ContractID'] = "not found"

    try:
        prepaidresidual['SubDealerID'] = prepaidresidual['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['SubDealerID'] = "not found"

    try:
        prepaidresidual['SubscriberID'] = prepaidresidual['SubscriberID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['SubscriberID'] = "not found"

    try:
        prepaidresidual['ServiceNo'] = prepaidresidual['ServiceNo'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['ServiceNo'] = "not found"

    try:
        prepaidresidual['RatePlanCode'] = prepaidresidual['RatePlanCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['RatePlanCode'] = "not found"

    try:
        prepaidresidual['MasterDealerCode'] = prepaidresidual['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['MasterDealerCode'] = "not found"

    try:
        prepaidresidual['SIM'] = prepaidresidual['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['SIM'] = "not found"

    try:
        prepaidresidual['IMEI'] = prepaidresidual['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['IMEI'] = "not found"

    try:
        prepaidresidual['FirstName'] = prepaidresidual['FirstName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['FirstName'] = "not found"

    try:
        prepaidresidual['LastName'] = prepaidresidual['LastName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['LastName'] = "not found"

    try:
        prepaidresidual['RefillAmt'] = prepaidresidual['RefillAmt'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepaidresidual['RefillAmt'] = 0.0

    try:
        prepaidresidual['DaysSinceActivation'] = prepaidresidual['DaysSinceActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepaidresidual['DaysSinceActivation'] = 0.0

    try:
        prepaidresidual["RefillDate"] = pd.to_datetime(prepaidresidual["RefillDate"].fillna(0))
    except:
        prepaidresidual['RefillDate'] = 0

    try:
        prepaidresidual['Month'] = prepaidresidual['Month'].str.replace("(" ,"").str.replace(")","")
        prepaidresidual["Month"] = pd.to_datetime(prepaidresidual["Month"].fillna(0))
    except:
        prepaidresidual['Month'] = 0

    try:
        prepaidresidual['FillAmount'] = prepaidresidual['FillAmount'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepaidresidual['FillAmount'] = 0.0

    try:
        prepaidresidual['TotalResidual'] = prepaidresidual['TotalResidual'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepaidresidual['TotalResidual'] = 0.0


    try:
        prepaidresidual['ResidualPCT'] = prepaidresidual['ResidualPCT'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepaidresidual['ResidualPCT'] = 0.0


    try:
        prepaidresidual["BeginServiceDate"] = pd.to_datetime(prepaidresidual["BeginServiceDate"].fillna(0))
    except:
        prepaidresidual["BeginServiceDate"] = 0

    try:
        prepaidresidual['BillingPlan'] = prepaidresidual['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['BillingPlan'] = "not found"

    try:
        prepaidresidual['ProductCatDescription'] = prepaidresidual['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['ProductCatDescription'] = "not found"

    try:
        prepaidresidual['ProductCatDescription'] = prepaidresidual['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['ProductCatDescription'] = "not found"

    try:
        prepaidresidual['DealerCode'] = prepaidresidual['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['DealerCode'] = "not found"

    try:
        prepaidresidual['TransactionID'] = prepaidresidual['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['TransactionID'] = "not found"

    try:
        prepaidresidual['CheckNumber'] = prepaidresidual['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepaidresidual['CheckNumber'] = "not found"

    try:
        prepaidresidual['DealerName'] = prepaidresidual['DealerName'].astype(np.str)
    except:
        prepaidresidual['DealerName'] = "not found"


    cursor = cnxn.cursor()
    for index,row in prepaidresidual.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-PREPAID-RESIDUAL] ([SalesCode], [ContractID], [SubDealerID], [SubscriberID], [FirstName], [LastName], [RefillDate], [ServiceNo], [MarketCode], [RatePlanCode], [RefillAmt], [DaysSinceActivation], [DealerName], [MasterDealerCode], [CheckNumber], [Month], [SIM], [IMEI], [FillAmount], [TotalResidual], [ResidualPCT], [BeginServiceDate], [BillingPlan], [ProductCatDescription], [DealerCode], [TransactionID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['SalesCode'], row['ContractID'], row['SubDealerID'], row['SubscriberID'], row['FirstName'], row['LastName'], row['RefillDate'], row['ServiceNo'], row['MarketCode'], row['RatePlanCode'], row['RefillAmt'], row['DaysSinceActivation'], row['DealerName'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'], row["FillAmount"], row["TotalResidual"], row["ResidualPCT"], row["BeginServiceDate"], row["BillingPlan"], row["ProductCatDescription"], row["DealerCode"], row["TransactionID"])

        # cursor.execute("INSERT INTO [Test].[dbo].[DAILEY-PREPAID-RESIDUAL] ([IMEI]) VALUES(?)", row["IMEI"])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


############################################################################################
############################################################################################

try:
    prepayresidual = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\PREPAY-RESIDUAL.xlsx")

    try:
        prepayresidual['SERVICEUNIVERSALID'] = prepayresidual['SERVICEUNIVERSALID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['SERVICEUNIVERSALID'] = "not found"

    try:
        prepayresidual['SalesCode'] = prepayresidual['SalesCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['SalesCode'] = "not found"

    try:
        prepayresidual['DealerName'] = prepayresidual['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['DealerName'] = "not found"

    try:
        prepayresidual['LineOfServiceID'] = prepayresidual['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['LineOfServiceID'] = "not found"

    try:
        prepayresidual['CUSTOMERNAME'] = prepayresidual['CUSTOMERNAME'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['CUSTOMERNAME'] = "not found"

    try:
        prepayresidual['ServiceNumber'] = prepayresidual['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['ServiceNumber'] = "not found"

    try:
        prepayresidual['MARKETCODE'] = prepayresidual['MARKETCODE'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['MARKETCODE'] = "not found"

    try:
        prepayresidual['MasterDealerCode'] = prepayresidual['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['MasterDealerCode'] = "not found"

    try:
        prepayresidual['BillingPlan'] = prepayresidual['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['BillingPlan'] = "not found"

    try:
        prepayresidual['ContractID'] = prepayresidual['ContractID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['ContractID'] = "not found"

    try:
        prepayresidual['CheckNumber'] = prepayresidual['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['CheckNumber'] = "not found"

    try:
        prepayresidual['SubDealerID'] = prepayresidual['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['SubDealerID'] = "not found"

    try:
        prepayresidual['ResidualType'] = prepayresidual['ResidualType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['ResidualType'] = "not found"

    try:
        prepayresidual['Month'] = prepayresidual['Month'].astype(np.str).replace('\.0', '', regex=True)
        prepayresidual["Month"] = pd.to_datetime(prepayresidual["Month"].fillna(0))
    except:
        prepayresidual['Month'] = 0

    try:
        prepayresidual['SIM'] = prepayresidual['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['SIM'] = "not found"

    try:
        prepayresidual['IMEI'] = prepayresidual['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['IMEI'] = "not found"

    try:
        prepayresidual['MonthlyAccess'] = prepayresidual['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepayresidual['MonthlyAccess'] = 0.0

    try:
        prepayresidual['ResidualPercent'] = prepayresidual['ResidualPercent'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepayresidual['ResidualPercent'] = 0.0

    try:
        prepayresidual['MonthsSinceLastActivation'] = prepayresidual['MonthsSinceLastActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepayresidual['MonthsSinceLastActivation'] = 0.0

    try:
        prepayresidual["BEGSERVDATE"] = pd.to_datetime(prepayresidual["BEGSERVDATE"].fillna(0))
    except:
        prepayresidual['BEGSERVDATE'] = 0

    try:
        prepayresidual['DealerName'] = prepayresidual['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        prepayresidual['DealerName'] = "not found"

    try:
        prepayresidual["DateString"] = pd.to_datetime(prepayresidual["DateString"].fillna(0))
    except:
        prepayresidual['DateString'] = 0

    try:
        prepayresidual['TotalResidual'] = prepayresidual['TotalResidual'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        prepayresidual['TotalResidual'] = 0.0

    try:
        prepayresidual['ProductCatDescription'] = prepayresidual['ProductCatDescription'].astype(np.str)
    except:
        prepayresidual['ProductCatDescription'] = "not found"

    try:
        prepayresidual["SubBaseStartDate"] = pd.to_datetime(prepayresidual["SubBaseStartDate"].fillna(0))
    except:
        prepayresidual['SubBaseStartDate'] = 0


    ## DATABASE
    cursor = cnxn.cursor()
    for index,row in prepayresidual.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-PREPAY-RESIDUAL] ([SERVICEUNIVERSALID], [SalesCode], [CUSTOMERNAME], [BEGSERVDATE], [LineOfServiceID], [ServiceNumber], [MARKETCODE], [BillingPlan], [MonthlyAccess], [ResidualPercent], [ContractID], [SubDealerID], [ResidualType], [MonthsSinceLastActivation], [MasterDealerCode], [CheckNumber], [Month], [SIM],[IMEI],[DealerName],[DateString],[TotalResidual],[ProductCatDescription],[SubBaseStartDate]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['SERVICEUNIVERSALID'], row['SalesCode'], row['CUSTOMERNAME'], row['BEGSERVDATE'], row['LineOfServiceID'], row['ServiceNumber'], row['MARKETCODE'], row['BillingPlan'], row['MonthlyAccess'], row['ResidualPercent'], row['ContractID'], row['SubDealerID'], row['ResidualType'], row['MonthsSinceLastActivation'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SIM'], row['IMEI'], row['DealerName'],row['DateString'],row['TotalResidual'],row['ProductCatDescription'],row['SubBaseStartDate'])

        # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PREPAY-RESIDUAL] ([ContractID]) VALUES(?)", row["ContractID"])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


############################################################################################
############################################################################################

try:
    pb = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\PB.xlsx")

    try:
        pb['ServiceUniversalID'] = pb['ServiceUniversalID'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ServiceUniversalID'] = "not found"

    try:
        pb['DealerCode'] = pb['DealerCode'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['DealerCode'] = "not found"

    try:
        pb['DealerName'] = pb['DealerName'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['DealerName'] = "not found"

    try:
        pb['IMEI'] = pb['IMEI'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['IMEI'] = "not found"

    try:
        pb['PlanCode'] = pb['PlanCode'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['PlanCode'] = "not found"

    try:
        pb['MarketCode'] = pb['MarketCode'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['MarketCode'] = "not found"

    try:
        pb['ProductType'] = pb['ProductType'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ProductType'] = "not found"

    try:
        pb['ActivityType'] = pb['ActivityType'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ActivityType'] = "not found"

    try:
        pb['ServiceNumber'] = pb['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ServiceNumber'] = "not found"

    try:
        pb['CustomerName'] = pb['CustomerName'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['CustomerName'] = "not found"

    try:
        pb['InvoiceNumber'] = pb['InvoiceNumber'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['InvoiceNumber'] = "not found"

    try:
        pb['BAN'] = pb['BAN'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['BAN'] = "not found"

    try:
        pb['DealerCode'] = pb['DealerCode'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['DealerCode'] = "not found"

    try:
        pb['ServiceNumber'] = pb['ServiceNumber'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ServiceNumber'] = "not found"

    try:
        pb['IMEI'] = pb['IMEI'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['IMEI'] = "not found"

    try:
        pb['BAN'] = pb['BAN'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['BAN'] = "not found"

    try:
        pb['SubDealerID'] = pb['SubDealerID'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['SubDealerID'] = "not found"

    try:
        pb['ActivatingStoreID'] = pb['ActivatingStoreID'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ActivatingStoreID'] = "not found"

    try:
        pb['ContractID'] = pb['ContractID'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ContractID'] = "not found"

    try:
        pb['MasterDealerCode'] = pb['MasterDealerCode'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['MasterDealerCode'] = "not found"

    try:
        pb['CheckNumber'] = pb['CheckNumber'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['CheckNumber'] = "not found"

    try:
        pb['PerformanceBonusType'] = pb['PerformanceBonusType'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['PerformanceBonusType'] = "not found"

    try:
        pb['PerformanceBonusName'] = pb['PerformanceBonusName'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['PerformanceBonusName'] = "not found"

    try:
        pb['ProductDescription'] = pb['ProductDescription'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['ProductDescription'] = "not found"

    try:
        pb['PerformanceBonus2Category'] = pb['PerformanceBonus2Category'].astype(str).replace('\.0', '', regex=True)
    except:
        pb['PerformanceBonus2Category'] = "not found"

    try:
        pb['Qty'] = pb['Qty'].fillna(0).astype(np.int).replace('\.0', '', regex=True)
    except:
        pb['Qty'] = 0

    try:
        pb['MonthlyAccess'] = pb['MonthlyAccess'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        pb['MonthlyAccess'] = 0.0

    try:
        pb['CustomerPaidAmount'] = pb['CustomerPaidAmount'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        pb['CustomerPaidAmount'] = 0.0

    try:
        pb['NUM'] = pb['NUM'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        pb['NUM'] = 0.0

    try:
        pb['DEN'] = pb['DEN'].fillna(0).astype(np.float64).replace('\.0', '', regex=True)
    except:
        pb['DEN'] = 0.0

    try:
        pb['SIM'] = pb['SIM'].fillna(0).astype(np.int64)
        pb['SIM'] = pb['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        pb['SIM'] = 0

    # pb.replace([np.nan], [""], inplace=True)

    ### DATABASE
    cursor = cnxn.cursor()
    for index,row in pb.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[DAILY-PB] ([ServiceUniversalID],[DealerCode],[DealerName],[MonthlyAccess],[PlanCode],[MarketCode],[ProductType],[ActivityType],[ActDate],[DeactDate], [ReactDate], [ServiceNumber], [CustomerName], [InvoiceNumber], [SIM], [IMEI], [BAN], [CustomerPaidAmount], [Qty], [SubDealerID], [ActivatingStoreID], [ContractID], [Month], [MasterDealerCode], [CheckNumber], [PerformanceBonusType], [PerformanceBonusName], [NUM], [DEN], [ProductDescription], [EffectiveCalcDate], [PerformanceBonus2Category]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['ServiceUniversalID'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['ReactDate'], row['ServiceNumber'], row['CustomerName'], row['InvoiceNumber'], row['SIM'], row['IMEI'], row['BAN'], row['CustomerPaidAmount'], row['Qty'], row['SubDealerID'], row['ActivatingStoreID'], row['ContractID'], row['Month'], row['MasterDealerCode'], row['CheckNumber'], row['PerformanceBonusType'], row['PerformanceBonusName'], row['NUM'], row['DEN'], row['ProductDescription'], str(row['EffectiveCalcDate']), row['PerformanceBonus2Category'])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


############################################################################################
############################################################################################

try:
    spiff = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\SPIFF.xlsx")

    try:
        spiff['ServiceUniversalID'] = spiff['ServiceUniversalID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ServiceUniversalID'] = "not found"

    try:
        spiff['CAPID'] = spiff['CAPID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CAPID'] = "not found"

    try:
        spiff['CAPDescription'] = spiff['CAPDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CAPDescription'] = "not found"

    try:
        spiff['SpiffID'] = spiff['SpiffID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SpiffID'] = "not found"

    try:
        spiff['SpiffDescription'] = spiff['SpiffDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SpiffDescription'] = "not found"

    try:
        spiff['DealerCode'] = spiff['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['DealerCode'] = "not found"

    try:
        spiff['DealerName'] = spiff['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['DealerName'] = "not found"

    try:
        spiff['PlanCode'] = spiff['PlanCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['PlanCode'] = "not found"

    try:
        spiff['MarketCode'] = spiff['MarketCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['MarketCode'] = "not found"

    try:
        spiff['CommMarketCode'] = spiff['CommMarketCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CommMarketCode'] = "not found"

    try:
        spiff['ProductType'] = spiff['ProductType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ProductType'] = "not found"

    try:
        spiff['ActivityType'] = spiff['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ActivityType'] = "not found"

    try:
        spiff['SameMonth'] = spiff['SameMonth'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SameMonth'] = "not found"

    try:
        spiff['LineOfServiceID'] = spiff['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['LineOfServiceID'] = "not found"

    try:
        spiff['ServiceNumber'] = spiff['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ServiceNumber'] = "not found"

    try:
        spiff['CustomerName'] = spiff['CustomerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CustomerName'] = "not found"

    try:
        spiff['SIMM'] = spiff['SIMM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SIMM'] = "not found"

    try:
        spiff['IMEI'] = spiff['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['IMEI'] = "not found"

    try:
        spiff['BAN'] = spiff['BAN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['BAN'] = "not found"

    try:
        spiff['CreditType'] = spiff['CreditType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CreditType'] = "not found"

    try:
        spiff['CreditClass'] = spiff['CreditClass'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CreditClass'] = "not found"

    try:
        spiff['SpiffGroup'] = spiff['SpiffGroup'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SpiffGroup'] = "not found"

    try:
        spiff['HOTI'] = spiff['HOTI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['HOTI'] = "not found"

    try:
        spiff['SubDealerID'] = spiff['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['SubDealerID'] = "not found"

    try:
        spiff['ProductCatDescription'] = spiff['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ProductCatDescription'] = "not found"

    try:
        spiff['MasterDealerCode'] = spiff['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['MasterDealerCode'] = "not found"

    try:
        spiff['Month'] = spiff['Month'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['Month'] = "not found"

    try:
        spiff['CheckNumber'] = spiff['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['CheckNumber'] = "not found"

    try:
        spiff['AdditionalDescription'] = spiff['AdditionalDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['AdditionalDescription'] = "not found"

    try:
        spiff['AccountTypeID'] = spiff['AccountTypeID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['AccountTypeID'] = "not found"

    try:
        spiff['AccountSubTypeID'] = spiff['AccountSubTypeID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['AccountSubTypeID'] = "not found"

    try:
        spiff['ActivatingStoreID'] = spiff['ActivatingStoreID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ActivatingStoreID'] = "not found"

    try:
        spiff['ProInstall'] = spiff['ProInstall'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ProInstall'] = "not found"

    try:
        spiff['Id'] = spiff['Id'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['Id'] = "not found"

    try:
        spiff['Payout'] = spiff['Payout'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        spiff['Payout'] = 0.0

    try:
        spiff['ContractID'] = spiff['ContractID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        spiff['ContractID'] = "not found"

    try:
        spiff['MonthlyAccess'] = spiff['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        spiff['MonthlyAccess'] = 0.0

    try:
        spiff['ContractTerm'] = spiff['ContractTerm'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        spiff['ContractTerm'] = 0.0

    default ="2010-10-01"

    try:
        spiff["ActDate"] = pd.to_datetime(spiff["ActDate"].fillna(default))
    except:
        spiff['ActDate'] = default

    try:
        spiff["DeactDate"] = pd.to_datetime(spiff["DeactDate"].fillna(default))
    except:
        spiff['DeactDate'] = default

    try:
        spiff["LastUpgradeDate"] = pd.to_datetime(spiff["LastUpgradeDate"].fillna(default))
    except:
        spiff['LastUpgradeDate'] = default

    try:
        spiff["LastSuspendDate"] = pd.to_datetime(spiff["LastSuspendDate"].fillna(default))
    except:
        spiff['LastSuspendDate'] = default

    try:
        spiff['Month'] = spiff['Month'].str.replace("(" ,"").str.replace(")","")
        spiff["Month"] = pd.to_datetime(spiff["Month"].fillna(default))
    except:
        spiff['Month'] = default


    ## DATABASE
    cursor = cnxn.cursor()
    for index,row in spiff.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-SPIFF] ([ServiceUniversalID], [CAPID], [CAPDescription], [SpiffID], [SpiffDescription], [DealerCode], [DealerName], [MonthlyAccess], [PlanCode], [MarketCode], [CommMarketCode], [ProductType], [ActivityType], [ActDate], [DeactDate], [SameMonth], [LineOfServiceID], [ServiceNumber], [CustomerName], [SIMM], [IMEI],[BAN], [ContractTerm], [CreditType], [CreditClass], [LastSuspendDate], [SpiffGroup], [HOTI], [SubDealerID], [ProductCatDescription] , [MasterDealerCode], [Month], [CheckNumber], [AdditionalDescription], [AccountTypeID], [AccountSubTypeID], [LastUpgradeDate], [ActivatingStoreID], [ProInstall], [Id], [Payout],  [ContractID]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['ServiceUniversalID'], row['CAPID'], row['CAPDescription'], row['SpiffID'], row['SpiffDescription'], row['DealerCode'], row['DealerName'], row['MonthlyAccess'], row['PlanCode'], row['MarketCode'], row['CommMarketCode'], row['ProductType'], row['ActivityType'], row['ActDate'], row['DeactDate'], row['SameMonth'], row['LineOfServiceID'], row['ServiceNumber'], row['CustomerName'], row['SIMM'], row['IMEI'], row['BAN'], row['ContractTerm'], row['CreditType'], row['CreditClass'], row['LastSuspendDate'], row['SpiffGroup'], row['HOTI'], row['SubDealerID'], row['ProductCatDescription'], row['MasterDealerCode'], row['Month'], row['CheckNumber'], row['AdditionalDescription'], row['AccountTypeID'], row['AccountSubTypeID'], row['LastUpgradeDate'], row['ActivatingStoreID'], row['ProInstall'], row['Id'], row['Payout'], row['ContractID'])

        # cursor.execute("INSERT INTO [Test].[dbo].[DAILY-SPIFF] ([LastSuspendDate]) VALUES(?)", row["LastSuspendDate"])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


############################################################################################
############################################################################################

try:
    residual = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\RESIDUAL.xlsx")

    try:
        residual['SERVICEUNIVERSALID'] = residual['SERVICEUNIVERSALID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['SERVICEUNIVERSALID'] = "not found"

    try:
        residual['DealerCode'] = residual['DealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['DealerCode'] = "not found"

    try:
        residual['DealerName'] = residual['DealerName'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['DealerName'] = "not found"

    try:
        residual['CUSTOMERNAME'] = residual['CUSTOMERNAME'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['CUSTOMERNAME'] = "not found"

    try:
        residual['BAN'] = residual['BAN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['BAN'] = "not found"

    try:
        residual['LineOfServiceID'] = residual['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['LineOfServiceID'] = "not found"

    try:
        residual['ServiceNumber'] = residual['ServiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['ServiceNumber'] = "not found"

    try:
        residual['MARKETCODE'] = residual['MARKETCODE'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['MARKETCODE'] = "not found"

    try:
        residual['BillingPlan'] = residual['BillingPlan'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['BillingPlan'] = "not found"

    try:
        residual['ContractID'] = residual['ContractID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['ContractID'] = "not found"

    try:
        residual['SubDealerID'] = residual['SubDealerID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['SubDealerID'] = "not found"

    try:
        residual['ResidualType'] = residual['ResidualType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['ResidualType'] = "not found"

    try:
        residual['MonthsSinceLastActivation'] = residual['MonthsSinceLastActivation'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['MonthsSinceLastActivation'] = "not found"

    try:
        residual['ProductCatDescription'] = residual['ProductCatDescription'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['ProductCatDescription'] = "not found"

    try:
        residual['MasterDealerCode'] = residual['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['MasterDealerCode'] = "not found"

    try:
        residual['CheckNumber'] = residual['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['CheckNumber'] = "not found"

    try:
        residual['Month'] = residual['Month'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['Month'] = "not found"

    try:
        residual['SIM'] = residual['SIM'].fillna(0).astype(np.int64)
        residual['SIM'] = residual['SIM'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['SIM'] = "not found"

    try:
        residual['IMEI'] = residual['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        residual['IMEI'] = "not found"

    try:
        residual['MonthsSinceLastActivation'] = residual['MonthsSinceLastActivation'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        residual['MonthsSinceLastActivation'] = 0.0

    try:
        residual['MonthlyAccess'] = residual['MonthlyAccess'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        residual['MonthlyAccess'] = 0.0

    try:
        residual['TotalResidual'] = residual['TotalResidual'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        residual['TotalResidual'] = 0.0

    try:
        residual['ResidualPercent'] = residual['ResidualPercent'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        residual['ResidualPercent'] = 0.0

    try:
        residual["SubBaseStartDate"] = pd.to_datetime(residual["SubBaseStartDate"].fillna(0))
    except:
        residual['SubBaseStartDate'] = 0

    try:
        residual["BEGSERVDATE"] = pd.to_datetime(residual["BEGSERVDATE"].fillna(0))
    except:
        residual['BEGSERVDATE'] = 0


    ## DATABASE
    cursor = cnxn.cursor()
    for index,row in residual.iterrows():
        cursor.execute("INSERT INTO [Test].[dbo].[ALLDETAILS-RESIDUAL_NEW] ([SERVICEUNIVERSALID], [DealerCode], [DealerName], [CUSTOMERNAME], [BAN], [BEGSERVDATE], [LineOfServiceID], [ServiceNumber], [MARKETCODE], [BillingPlan], [MonthlyAccess], [TotalResidual], [ResidualPercent], [ContractID], [SubDealerID], [ResidualType], [MonthsSinceLastActivation], [ProductCatDescription], [MasterDealerCode], [CheckNumber], [Month], [SubBaseStartDate], [SIM], [IMEI]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        , row['SERVICEUNIVERSALID'], row['DealerCode'], row['DealerName'], row['CUSTOMERNAME'], row['BAN'], row['BEGSERVDATE'], row['LineOfServiceID'], row['ServiceNumber'], row['MARKETCODE'], row['BillingPlan'], row['MonthlyAccess'], row['TotalResidual'], row['ResidualPercent'], row['ContractID'], row['SubDealerID'], row['ResidualType'], row['MonthsSinceLastActivation'], row['ProductCatDescription'], row['MasterDealerCode'], row['CheckNumber'], row['Month'], row['SubBaseStartDate'], row['SIM'], row['IMEI'])

    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass


####################################################################################################
####################################################################################################

try:
    handset = pd.read_excel(r"C:\xampp\htdocs\Terminal\Daily All Details\all\HANDSET.xlsx")

    try:
        handset["TransactionDate"] = pd.to_datetime(handset["TransactionDate"])
    except:
        handset["TransactionDate"] = 0

    try:
        handset['TransactionID'] = handset['TransactionID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["TransactionID"] = "not found"

    try:
        handset['DiscountChargeBack'] = handset['DiscountChargeBack'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["DiscountChargeBack"] = 0.0

    try:
        handset['StoreID'] = handset['StoreID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["StoreID"] = "not found"

    try:
        handset['InvoiceNumber'] = handset['InvoiceNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["InvoiceNumber"] = "not found"

    try:
        handset['SalesPersonCode'] = handset['SalesPersonCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["SalesPersonCode"] = "not found"

    try:
        handset['MSISDN'] = handset['MSISDN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["MSISDN"] = "not found"

    try:
        handset['BAN'] = handset['BAN'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["BAN"] = "not found"

    try:
        handset['IMEI'] = handset['IMEI'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["IMEI"] = "not found"

    try:
        handset['SKU'] = handset['SKU'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["SKU"] = "not found"

    try:
        handset['POSType'] = handset['POSType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["POSType"] = "not found"

    try:
        handset['ActivityType'] = handset['ActivityType'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["ActivityType"] = "not found"

    try:
        handset['LineOfServiceID'] = handset['LineOfServiceID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["LineOfServiceID"] = "not found"

    try:
        handset['SAPTransTypeCode'] = handset['SAPTransTypeCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["SAPTransTypeCode"] = "not found"

    try:
        handset['ProductCategory'] = handset['ProductCategory'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["ProductCategory"] = "not found"

    try:
        handset['MasterDealerCode'] = handset['MasterDealerCode'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["MasterDealerCode"] = "not found"

    try:
        handset['Month'] = handset['Month'].str.replace("(", "").str.replace(")", "")
        handset["Month"] = pd.to_datetime(handset["Month"].fillna(0))
    except:
        handset["Month"] = 0

    try:
        handset['CheckNumber'] = handset['CheckNumber'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["CheckNumber"] = "not found"

    try:
        handset['Source'] = handset['Source'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["Source"] = "not found"

    try:
        handset['OverrideReason'] = handset['OverrideReason'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["OverrideReason"] = "not found"

    try:
        handset['QTY'] = handset['QTY'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["QTY"] = 0.0

    try:
        handset['EIPIndicator'] = handset['EIPIndicator'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["EIPIndicator"] = 0.0

    try:
        handset['ReturnCode'] = handset['ReturnCode'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["ReturnCode"] = 0.0

    try:
        handset['EIP1stPayment'] = handset['EIP1stPayment'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["EIP1stPayment"] = 0.0

    try:
        handset['EIPPlanID'] = handset['EIPPlanID'].fillna(0).astype(np.int64)
        handset['EIPPlanID'] = handset['EIPPlanID'].astype(np.str).replace('\.0', '', regex=True)
    except:
        handset["EIPPlanID"] = "not found"

    try:
        handset['MSRP'] = handset['MSRP'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["MSRP"] = 0.0

    try:
        handset['SellingPrice'] = handset['SellingPrice'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["SellingPrice"] = 0.0

    try:
        handset['CustomerPaidAmt'] = handset['CustomerPaidAmt'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["CustomerPaidAmt"] = 0.0

    try:
        handset['PriceOffered'] = handset['PriceOffered'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["PriceOffered"] = 0.0

    try:
        handset['OverrideReason'] = handset['OverrideReason'].fillna(0).astype(np.float).replace('\.0', '', regex=True)
    except:
        handset["OverrideReason"] = 0.0

    ## DATABASE
    cursor = cnxn.cursor()
    for index, row in handset.iterrows():
        cursor.execute(
            "INSERT INTO [Test].[dbo].[ALLDETAILS-HANDSET] ([TransactionID], [TransactionDate], [StoreID], [InvoiceNumber], [MSRP], [SellingPrice], [CustomerPaidAmt], [PriceOffered], [SalesPersonCode], [SKU], [IMEI], [BAN], [MSISDN], [POSType], [ActivityType], [LineOfServiceID], [SAPTransTypeCode], [ProductCategory], [ProductDescription], [QTY], [OverrideReason], [ReturnCode], [EIPIndicator], [EIP1stPayment], [EIPPlanID], [MasterDealerCode], [Month], [CheckNumber], [Source], [DiscountChargeBack]) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            , row['TransactionID'], row['TransactionDate'], row['StoreID'], row['InvoiceNumber'], row['MSRP'],
            row['SellingPrice'], row['CustomerPaidAmt'], row['PriceOffered'], row['SalesPersonCode'], row['SKU'],
            row['IMEI'], row['BAN'], row['MSISDN'], row['POSType'], row['ActivityType'], row['LineOfServiceID'],
            row['SAPTransTypeCode'], row['ProductCategory'], row['ProductDescription'], row['QTY'], row['OverrideReason'],
            row['ReturnCode'], row['EIPIndicator'], row['EIP1stPayment'], row['EIPPlanID'], row['MasterDealerCode'],
            row['MasterDealerCode'], row['Month'], row['Source'], row["DiscountChargeBack"])
    cnxn.commit()
    cursor.close()
    print("done")

except:
    pass