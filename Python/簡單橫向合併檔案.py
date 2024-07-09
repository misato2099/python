import glob
import os
import pandas as pd

##################################################
#########################合併#####################
##################################################

files_joined = os.path.join(
    'D:\\User_Data\\Desktop\\WORK\\稅籍\\正式作業\\地標與三級發布區\\三級發布區\\全部', '*.csv')
    
list_files = glob.glob(files_joined)

mdf = pd.concat(map(pd.read_csv, list_files), axis=1, ignore_index=False) #改成橫向合併，回家找檔案
mdf = mdf.T.drop_duplicates(keep='first').T #刪走重複欄

# 儲存母檔
mdf.to_csv('宜蘭縣_三級發布區.csv', index=False, encoding='utf-8-sig')

