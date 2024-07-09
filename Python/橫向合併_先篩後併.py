#發票數量
import glob
import os
import pandas as pd

city = "宜蘭縣"

yearlist = [{"1月":"receipt_10501", "2月":"receipt_10502", "3月":"receipt_10503", "4月":"receipt_10504", "5月":"receipt_10505", "6月":"receipt_10506", 
            "7月":"receipt_10507", "8月":"receipt_10508", "9月":"receipt_10509", "10月":"receipt_10510", "11月":"receipt_10511", "12月":"receipt_10512"}, 
            {"1月":"receipt_10601", "2月":"receipt_10602", "3月":"receipt_10603", "4月":"receipt_10604", "5月":"receipt_10605", "6月":"receipt_10606", 
            "7月":"receipt_10607", "8月":"receipt_10608", "9月":"receipt_10609", "10月":"receipt_10610", "11月":"receipt_10611", "12月":"receipt_10612"}, 
            {"1月":"receipt_10701", "2月":"receipt_10702", "3月":"receipt_10703", "4月":"receipt_10704", "5月":"receipt_10705", "6月":"receipt_10706", 
            "7月":"receipt_10707", "8月":"receipt_10708", "9月":"receipt_10709", "10月":"receipt_10710", "11月":"receipt_10711", "12月":"receipt_10712"}, 
            {"1月":"receipt_10801", "2月":"receipt_10802", "3月":"receipt_10803", "4月":"receipt_10804", "5月":"receipt_10805", "6月":"receipt_10806", 
            "7月":"receipt_10807", "8月":"receipt_10808", "9月":"receipt_10809", "10月":"receipt_10810", "11月":"receipt_10811", "12月":"receipt_10812"}]

i = 0

sourceFolderPath = os.path.join(os.path.dirname(__file__), '發票數量')
if not os.path.isdir(sourceFolderPath):
    os.makedirs(sourceFolderPath)
savingFolderPath = os.path.join(os.path.dirname(__file__), '整理檔\\發票數量')
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
            df = df.loc[df['COUN_NA'].str.contains(city)]
            #print(df)
            savingFilePath = os.path.join(savingFolderPath, file)
            df.to_csv(savingFilePath,
                       index=False, encoding='utf-8-sig')
            i += 1

##################################################
#########################合併#####################
##################################################

files_joined = os.path.join(
    'D:\\User_Data\\Desktop\\WORK\\稅籍\\正式作業\\地標與三級發布區\\三級發布區\\電子發票資料\\待合併原始檔\\整理檔\\發票數量', '*.csv')
    
list_files = glob.glob(files_joined)

mdf = pd.concat(map(pd.read_csv, list_files), axis=1, ignore_index=False) #改成橫向合併，回家找檔案
mdf = mdf.T.drop_duplicates(keep='first').T #刪走重複欄

# 儲存母檔
mdf.to_csv(os.path.join(mergeFolderPath,
           f'{city}_receipt.csv'), index=False, encoding='utf-8-sig')

