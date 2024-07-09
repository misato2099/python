# 註：BGMF009.sinica.09312.csv中原始資料有一筆資料遺漏營業人名稱，需手動填補：富群超商股份有限公司第866分公司
import re
from cleaning import strQ2B2
from cleaning import strQ2B
import glob
import os
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

city = "宜蘭縣"

#插入每年營業狀況：目前無法在同一程式執行
#yearlist = ["open_09212", "open_09312", "open_09412", "open_09512", "open_09612", "open_09712", "open_09812",
#            "open_09906", "open_09912", "open_10006", "open_10012", "open_10106", "open_10112", "open_10206",
#            "open_10212", "open_10306", "open_10312", "open_10406", "open_10412", "open_10506", "open_10512",
#            "open_10606", "open_10612", "open_10706", "open_10712", "open_10806", "open_10812", "open_10906",
#            "open_10912", "open_11006"]
#i = 0

openst = {"營業中": "1"}



keyword = '統―超商|統-超商|統一超商|來來超商|全家便利商店|萊爾富國際|富群超商|富羣超商|眾利超商|統超商'

columnlist1 = ['統一編號', '營業人名稱',
               '資本額', '設立日期（YYYMMDD）', '是否使用統一發票（Y/N）',
               '行業代號', '名稱', '行業代號1', '名稱1',
               '行業代號2', '名稱2', '行業代號3', '名稱3',
               '營業狀況（營業中、停業中、停業以外之非營業中）', '多餘1']
columnlist2 = ['營業人名稱',
               '資本額', '設立日期（YYYMMDD）', '是否使用統一發票（Y/N）',
               '行業代號', '名稱', '行業代號1', '名稱1',
               '行業代號2', '名稱2', '行業代號3', '名稱3',
               '營業狀況（營業中、停業中、停業以外之非營業中）', '多餘1', '多餘2']
columnlist3 = ['統一編號', '營業人名稱',
               '資本額', '設立日期（YYYMMDD）', '是否使用統一發票（Y/N）',
               '行業代號', '名稱', '行業代號1', '名稱1',
               '行業代號2', '名稱2', '行業代號3', '名稱3',
               '營業狀況（營業中、停業中、停業以外之非營業中）']
columnlist4 = ['資本額', '設立日期（YYYMMDD）', '是否使用統一發票（Y/N）',
               '行業代號', '名稱', '行業代號1', '名稱1',
               '行業代號2', '名稱2', '行業代號3', '名稱3',
               '營業狀況（營業中、停業中、停業以外之非營業中）', '多餘1', '多餘2']

filelist = []

sourceFolderPath = os.path.join(os.path.dirname(__file__), '歷年資料原檔案')
savingFolderPath = os.path.join(os.path.dirname(__file__), '合併檔')

##################################################
#######################合併母檔####################
##################################################

files_joined = os.path.join(
    'D:\\User_Data\\Desktop\\WORK\\稅籍\\正式作業\\解釋步驟\\母檔原檔案', '*.csv')
list_files = glob.glob(files_joined)
df0 = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
df0 = df0.dropna(subset=['營業人名稱'])
df0 = df0.reset_index(drop=True)
df0 = df0.loc[df0['營業人名稱'].str.contains(
    keyword)][df0['營業地址'].str.contains(city)]
adrs = []
names = []
# 整理營業地址格式
for adr in df0['營業地址']:
    str11 = strQ2B(adr).strip()
    str11 = re.sub(r"\d+F", '', str11)  # 刪除結尾的樓層(英數)
    str11 = re.sub("&", '', str11)  # 刪除結尾的樓層(英數)
    str11 = re.sub(r"[\d]、[\d]樓", '', str11)  # 刪除結尾的樓層(數字)
    str11 = re.sub(r"\d+樓", '', str11)  # 刪除結尾的樓層(數字)
    str11 = re.sub("-樓", '', str11)  # 刪除結尾的樓層(-短dash)
    str11 = re.sub("1段", "一段", str11)
    str11 = re.sub("2段", "二段", str11)
    str11 = re.sub("3段", "三段", str11)
    str11 = re.sub("4段", "四段", str11)
    str11 = re.sub("5段", "五段", str11)
    str11 = re.sub("6段", "六段", str11)
    str11 = re.sub("7段", "七段", str11)
    str11 = re.sub("8段", "八段", str11)
    str11 = re.sub("9段", "九段", str11)
    str11 = re.sub(r"[^u4E00-u9FA5]樓", '', str11)  # 刪除結尾的樓層(中文)
    str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]里",
                   '', str11)  # 刪除里
    str11 = re.sub(r"[^u4E00-u9FA5]里", '', str11)  # 刪除里
    str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]村",
                   '', str11)  # 刪除結尾的樓層(中文)
    str11 = re.sub(r"[^u4E00-u9FA5]村", '', str11)  # 刪除村
    str11 = re.sub(r"\d+鄰", '', str11)  # 刪除鄰
    str11 = re.sub(
        r"[^u4E00-u9FA5]、[^u4E00-u9FA5]樓", '', str11)  # 刪除多層樓層(中文)
    adrs.append(str11)
# 整理營業人名稱格式
for name in df0['營業人名稱']:
    str12 = strQ2B2(name).strip()
    names.append(str12)
# 更新資料
df0['營業地址'] = adrs
df0['營業人名稱'] = names

# 儲存母檔
savingFolderPath = os.path.join(os.path.dirname(
    __file__), '合併檔')  # 建立儲存路徑
if not os.path.isdir(savingFolderPath):
    os.makedirs(savingFolderPath)
df0.to_csv(os.path.join('D:\\User_Data\Desktop\\WORK\\稅籍\\正式作業\\解釋步驟\\合併檔',
           'originfile.csv'), index=False, encoding='utf-8-sig')

##################################################
#######################整理子檔####################
##################################################
for root, folders, files in os.walk(sourceFolderPath):
    for file in sorted(files):
        if file[0] != '.' and file[0] != '~' and file[-3:] == 'csv':
            filePath = os.path.join(root, file)
            df1 = pd.read_csv(filePath, engine='python',
                              sep='delimiter', header=None, encoding='utf-8-sig')
            df1 = df1.iloc[1:, :]
            df1 = df1[0].str.split(',', expand=True)
            # 填補刪資料後的空列號，括號內drop=True則換掉，空格或False則保留兩條
            df1 = df1.reset_index(drop=True)
            df1 = df1.rename(columns={0: '營業地址', 1: '統一編號', 2: '營業人名稱',
                                      3: '資本額', 4: '設立日期（YYYMMDD）', 5: '是否使用統一發票（Y/N）',
                                      6: '行業代號', 7: '名稱', 8: '行業代號1', 9: '名稱1',
                                      10: '行業代號2', 11: '名稱2', 12: '行業代號3', 13: '名稱3',
                                      14: '營業狀況（營業中、停業中、停業以外之非營業中）', 15: '多餘1', 16: '多餘2'})

######### 第一排凸行##########
            df1['多餘1'] = df1['多餘1'].replace('', None)
            filter1 = df1['多餘1'].notnull()
            df2 = df1[filter1]  # 只顯示有問題結果
            df2['統一編號'] = df2['統一編號'].replace('', '')  # 將所有隱藏空格轉化為無
            df2['營業地址'] = df2['營業地址']+"，"+df2['統一編號']
            df2['營業地址'] = df2['營業地址'].str.rstrip('，')

            for i, j in zip(columnlist1, columnlist2):
                df2[i] = df2[j]

######### 第二排凸行##########
            df1['多餘2'] = df1['多餘2'].replace('', None)
            filter2 = df1['多餘2'].notnull()
            df3 = df1[filter2]  # 只顯示有問題結果
            df3['統一編號'] = df3['統一編號'].replace('', '')  # 將所有隱藏空格轉化為無
            df3['營業人名稱'] = df3['營業人名稱'].replace('', '')  # 將所有隱藏空格轉化為無
            df3['營業地址'] = df3['營業地址']+"，"+df3['統一編號']+"，"+df3['營業人名稱']
            df3['營業地址'] = df3['營業地址'].str.rstrip('，')

            for k, l in zip(columnlist3, columnlist4):
                df3[k] = df3[l]
            df3['多餘2'] = None

# 合併資料框及刪除多餘重複列
            mdf = pd.concat([df1, df2, df3], axis=0)
            # 填補刪資料後的空列號，括號內drop=True則取代舊號，空格或False則新舊皆保留
            mdf = mdf.reset_index(drop=True)
            mdf = mdf.loc[mdf['營業人名稱'].str.contains('義美|全聯') == False]  # 篩選義美及全聯以外超商
            mdf = mdf.loc[mdf['營業地址'].str.contains(city)]  # 篩選地址包含宜蘭縣資料
            mdf = mdf[mdf['多餘1'].notnull() == False]
            mdf = mdf[mdf['多餘2'].notnull() == False]
            mdf = mdf.drop(columns=['多餘1', '多餘2'])  # 刪除空白的兩欄

# 整理
            adrs = []
            names = []
            # 整理營業地址格式
            for adr in mdf['營業地址']:
                str11 = strQ2B(adr).strip()
                str11 = re.sub(r"\d+F", '', str11)  # 刪除結尾的樓層(英數)
                str11 = re.sub("&", '', str11)  # 刪除結尾的樓層(英數)
                str11 = re.sub(r"[\d]、[\d]樓", '', str11)  # 刪除結尾的樓層(數字)
                str11 = re.sub(r"\d+樓", '', str11)  # 刪除結尾的樓層(數字)
                str11 = re.sub("-樓", '', str11)  # 刪除結尾的樓層(-短dash)
                str11 = re.sub("1段", "一段", str11)
                str11 = re.sub("2段", "二段", str11)
                str11 = re.sub("3段", "三段", str11)
                str11 = re.sub("4段", "四段", str11)
                str11 = re.sub("5段", "五段", str11)
                str11 = re.sub("6段", "六段", str11)
                str11 = re.sub("7段", "七段", str11)
                str11 = re.sub("8段", "八段", str11)
                str11 = re.sub("9段", "九段", str11)
                str11 = re.sub(r"[^u4E00-u9FA5]樓", '', str11)  # 刪除結尾的樓層(中文)
                str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]里",
                               '', str11)  # 刪除里
                str11 = re.sub(r"[^u4E00-u9FA5]里", '', str11)  # 刪除里
                str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]村",
                               '', str11)  # 刪除結尾的樓層(中文)
                str11 = re.sub(r"[^u4E00-u9FA5]村", '', str11)  # 刪除村
                str11 = re.sub(r"\d+鄰", '', str11)  # 刪除鄰
                str11 = re.sub(
                    r"[^u4E00-u9FA5]、[^u4E00-u9FA5]樓", '', str11)  # 刪除多層樓層(中文)
                adrs.append(str11)

            # 整理營業人名稱格式
            for name in mdf['營業人名稱']:
                str12 = strQ2B2(name).strip()
                names.append(str12)

            # 更新資料
            mdf['營業地址'] = adrs
            mdf['營業人名稱'] = names
            # 填補刪資料後的空列號，括號內drop=True則取代舊號，空格或False則新舊皆保留
            mdf = mdf.reset_index(drop=True)
            #mdf[yearlist[i]] = mdf['營業狀況（營業中、停業中、停業以外之非營業中）'].map(openst)

            # 儲存分檔
            savingFilePath = os.path.join(savingFolderPath, file)
            mdf.to_csv(savingFilePath,
                       index=False, encoding='utf-8-sig')
            #i += 1
