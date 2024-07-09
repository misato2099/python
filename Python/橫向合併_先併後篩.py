#銷售額
import glob
import os
import pandas as pd

city = "宜蘭縣"

sourceFolderPath = os.path.join(os.path.dirname(__file__), '電戶')
if not os.path.isdir(sourceFolderPath):
    os.makedirs(sourceFolderPath)
savingFolderPath = os.path.join(os.path.dirname(__file__), '整理檔\\電戶')
if not os.path.isdir(savingFolderPath):
    os.makedirs(savingFolderPath)
mergeFolderPath = os.path.join(os.path.dirname(
    __file__), '合併檔')
if not os.path.isdir(mergeFolderPath):
    os.makedirs(mergeFolderPath)

##################################################
#########################合併#####################
##################################################

files_joined = os.path.join(
    'D:\\User_Data\\Desktop\\WORK\\稅籍\\正式作業\\地標與三級發布區\\三級發布區\\水電資料\\電戶', '*.csv')
    
list_files = glob.glob(files_joined)

mdf = pd.concat(map(pd.read_csv, list_files), axis=1, ignore_index=False)
mdf = mdf.T.drop_duplicates(keep='first').T #刪走重複欄

mdf.columns.values[5:53] = ["pwusr_10501", "pwusr_10502", "pwusr_10503", "pwusr_10504", "pwusr_10505", "pwusr_10506", 
            "pwusr_10507", "pwusr_10508", "pwusr_10509", "pwusr_10510", "pwusr_10511", "pwusr_10512", 
            "pwusr_10601", "pwusr_10602", "pwusr_10603", "pwusr_10604", "pwusr_10605", "pwusr_10606", 
            "pwusr_10607", "pwusr_10608", "pwusr_10609", "pwusr_10610", "pwusr_10611", "pwusr_10612", 
            "pwusr_10701", "pwusr_10702", "pwusr_10703", "pwusr_10704", "pwusr_10705", "pwusr_10706", 
            "pwusr_10707", "pwusr_10708", "pwusr_10709", "pwusr_10710", "pwusr_10711", "pwusr_10712", 
            "pwusr_10801", "pwusr_10802", "pwusr_10803", "pwusr_10804", "pwusr_10805", "pwusr_10806", 
            "pwusr_10807", "pwusr_10808", "pwusr_10809", "pwusr_10810", "pwusr_10811", "pwusr_10812"]

# 儲存母檔
mdf.to_csv(os.path.join(mergeFolderPath,
           'merge_pwusr.csv'), index=False, encoding='utf-8-sig')

##################################################
#########################整理#####################
##################################################

df = pd.read_csv(os.path.join(mergeFolderPath,'merge_pwusr.csv'), encoding='utf-8-sig')
df = df.loc[df['COUN_NA'].str.contains(city)]
savingFilePath = os.path.join(mergeFolderPath, f'{city}_pwusr.csv')
df.to_csv(savingFilePath,
            index=False, encoding='utf-8-sig')





