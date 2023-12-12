import openpyxl

import os
import glob
import pandas as pd

# Path to the folder containing your Excel files
folder_path = 'fmcg_data'
l=[]
# Iterate through all Excel files in the folder
for file_name in glob.glob(os.path.join(folder_path, '*.xlsx')):
    # Rename the file
    wb = openpyxl.load_workbook(file_name)
    sh = wb.active

    c1 = sh['A1']
    data=sh['F58'].value
    lol=sh['E56'].value
    # elec=sh['F50'].value
    name=c1.value
    name=name.split(":")[-1].strip().lower()
    name=name.split(" ")
    new_file_name="_".join(name)
    print(new_file_name)
    temp=[]
    val=None
    try:
        val=float(float(data)/float(lol))
    except:
        val=None
    temp.append(new_file_name);temp.append(val);
    l.append(temp)

df = pd.DataFrame(l, columns = ['district', 'water_per']) 
df.to_csv("per_water.csv",index=False)