import pandas as pd

# 讀取原始檔案
df = pd.read_csv("store_fulllist.csv", encoding="utf-8-sig")  

# 建立新的資料框以儲存輸出結果
output_df = pd.DataFrame(columns=['period', 'COUNTYNAME', 'SE_total', 'FM_total', 'HF_total', 'OK_total'])

# 遍歷原始資料框
for column in df.columns:
    if 'open_' in column:
        # 提取年份（假設年份在 column 名稱的最後5個字符中）
        period = column[-5:]
        
        # 提取 countyname 的唯一值
        unique_countynames = df['COUNTYNAME'].unique()
        
        # 第一層迴圈: 每個countyname
        for countyname in unique_countynames:
            # 在每個countyname下篩選出欄位brand的唯一值
            unique_brands = df[df['COUNTYNAME'] == countyname]['brand'].unique()
            
            # 初始化各品牌的加總值
            SE_total, FM_total, HF_total, OK_total = 0, 0, 0, 0
            
            # 第二層迴圈: 每個brand
            for brand in unique_brands:
                brand_total = df[(df['COUNTYNAME'] == countyname) & (df['brand'] == brand)][column].sum()
                if brand == 'SE':
                    SE_total = brand_total
                elif brand == 'FM':
                    FM_total = brand_total
                elif brand == 'HF':
                    HF_total = brand_total
                elif brand == 'OK':
                    OK_total = brand_total
            
            # 將加總值加入到新的資料框中
            output_df = output_df.append({'period': period, 'COUNTYNAME': countyname, 'SE_total': SE_total,
                                          'FM_total': FM_total, 'HF_total': HF_total, 'OK_total': OK_total}, 
                                          ignore_index=True)

# 按照COUNTYNAME、然後按period從小到大排序
output_df = output_df.sort_values(by=['COUNTYNAME', 'period'])

# 重新設定索引
output_df.reset_index(drop=True, inplace=True)

# 儲存結果至新檔案
output_df.to_csv("store_output.csv", encoding="utf-8-sig", index=False)
