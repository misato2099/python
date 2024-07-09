#店家數量
import glob
import os
import pandas as pd

exclude_list = ['連江縣','金門縣','澎湖縣']

yearlist = [{"1月":"store_10501", "2月":"store_10502", "3月":"store_10503", "4月":"store_10504", "5月":"store_10505", "6月":"store_10506", 
            "7月":"store_10507", "8月":"store_10508", "9月":"store_10509", "10月":"store_10510", "11月":"store_10511", "12月":"store_10512"}, 
            {"1月":"store_10601", "2月":"store_10602", "3月":"store_10603", "4月":"store_10604", "5月":"store_10605", "6月":"store_10606", 
            "7月":"store_10607", "8月":"store_10608", "9月":"store_10609", "10月":"store_10610", "11月":"store_10611", "12月":"store_10612"}, 
            {"1月":"store_10701", "2月":"store_10702", "3月":"store_10703", "4月":"store_10704", "5月":"store_10705", "6月":"store_10706", 
            "7月":"store_10707", "8月":"store_10708", "9月":"store_10709", "10月":"store_10710", "11月":"store_10711", "12月":"store_10712"}, 
            {"1月":"store_10801", "2月":"store_10802", "3月":"store_10803", "4月":"store_10804", "5月":"store_10805", "6月":"store_10806", 
            "7月":"store_10807", "8月":"store_10808", "9月":"store_10809", "10月":"store_10810", "11月":"store_10811", "12月":"store_10812"}]

i = 0

sourceFolderPath = os.path.join(os.path.dirname(__file__), '店家數量')
if not os.path.isdir(sourceFolderPath):
    os.makedirs(sourceFolderPath)
savingFolderPath = os.path.join(os.path.dirname(__file__), '整理檔\\店家數量')
if not os.path.isdir(savingFolderPath):
    os.makedirs(savingFolderPath)
mergeFolderPath = os.path.join(os.path.dirname(
    __file__), '合併檔')
if not os.path.isdir(mergeFolderPath):
    os.makedirs(mergeFolderPath)

##################################################
#########################整理#####################
##################################################

for root, folders, files in os.walk(sourceFolderPath):
    for file in sorted(files):
        if file[0] != '.' and file[0] != '~' and file[-3:] == 'csv':
            filePath = os.path.join(root, file)
            df = pd.read_csv(filePath, encoding='utf-8-sig')
            df = df.sort_values(by=['CODE3'])
            df = df.rename(columns=yearlist[i])
            mask = ~df['COUN_NA'].isin(exclude_list)
            df = df.loc[mask]
            savingFilePath = os.path.join(savingFolderPath, file)
            df.to_csv(savingFilePath,
                       index=False, encoding='utf-8-sig')
            i += 1

##################################################
#########################合併#####################
##################################################

files_joined = os.path.join(
    r'\\140.109.121.110\nas\超商研究資料彙整\全台數據\四大資料\三級發布區\電子發票資料\待合併原始檔\整理檔\店家數量', '*.csv')
    
list_files = glob.glob(files_joined)

mdf = pd.concat(map(pd.read_csv, list_files), axis=1, ignore_index=False) #改成橫向合併，回家找檔案
mdf = mdf.T.drop_duplicates(keep='first').T #刪走重複欄

# 儲存母檔
mdf.to_csv(os.path.join(mergeFolderPath,
           f'taiwan_store.csv'), index=False, encoding='utf-8-sig')

