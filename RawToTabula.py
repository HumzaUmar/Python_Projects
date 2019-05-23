import glob
import shutil
import os
import fnmatch
from PyPDF2 import PdfFileReader
import tabula
from pathlib import Path
import pandas as pd
from pandas import ExcelWriter
import shutil
import pyodbc

pd.set_option('display.max_columns', 160000)
pd.set_option('display.width', 100000)


filelist = glob.glob(os.path.join(r'C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/format', "*.csv"))
for f in filelist:
    os.remove(f)

filelist = glob.glob(os.path.join(r'C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/blank', "*.csv"))
for f in filelist:
    os.remove(f)

filelist = glob.glob(os.path.join(r'C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/format', "*.xlsx"))
for f in filelist:
    os.remove(f)


dirpath = r"C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/"
dirpath2 = r"C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/format"
dirpath_blank = r'C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/blank'
countpdf = len(fnmatch.filter(os.listdir(dirpath), '*.pdf'))
source_files='C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/*.csv'
target_folder1='C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/Newfolder'
dir = glob.glob(r"C:/Users/RD1\Desktop/Task_Assigned/12-26-2018 rma sto/*.pdf")

a = 0
b = countpdf

for i in range(a, b):
        ful_file = dirpath + os.path.basename(dir[i])
        name_pdf = Path(ful_file).name
        full_pdf_path = dirpath+name_pdf
        pdf = PdfFileReader(open(ful_file,'rb'))
        countpdf = pdf.getNumPages()
        total = countpdf
        print(total)
        a1 = 0
        b1 = total
        for i in range(a1, b1):
            # print(ful_file)
            df1 = tabula.read_pdf(ful_file, multiple_tables=True, pages="all", guess=False)
            a1 = df1[i]
            if a1[1][8] == "TOTALS:":

                print('--------------')
                print(a1.to_csv(dirpath_blank + name_pdf + '(page#' + str(i + 1) + ')' + '.csv'))
                print('--------------')
            if a1[1][8] != "TOTALS:":

                print('**********')
                print(a1.to_csv(dirpath2 + name_pdf + '(page#' + str(i + 1) + ')' + '.csv'))
                print('**********')

