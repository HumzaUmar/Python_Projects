import pandas as pd
import os
import glob
import csv
pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)

fileexpo = glob.glob(r'C:\Users\RD1\Desktop\Task_Assigned\Pg_01 Task\expo')
files = glob.glob(r'C:\Users\RD1\Desktop\Task_Assigned\Pg_01 Task\test/*.csv')
files_len = len(files)
file_start = range(0, files_len)
ka = []
for p in file_start:
    pathfile = files[p]
    # print(pathfile)

dir = r'C:\Users\RD1\Desktop\Task_Assigned\Pg_01 Task\expo/'
for a in range(files_len):
    mydata = pd.read_csv(files[a])
    print(mydata.to_excel(dir+str(a)+'.xlsx'))