import pandas as pd

# 讀取原始檔案
df = pd.read_csv("residence_full.csv", encoding="utf-8-sig")  # 假設你的原始檔案是 CSV 格式的，如果是其他格式，請使用對應的函數來讀取

# 建立新的資料框以儲存輸出結果
output_df = pd.DataFrame(columns=['period', 'COUNTYNAME', 'pop_total'])

# 遍歷原始資料框
for column in df.columns:
    if 'pop_' in column:
        # 提取年份（假設年份在 column 名稱的最後5個字符中）
        period = column[-5:]
        
        # 計算每期每組 countyname 的數值加總
        temp_df = df.groupby(['COUNTYNAME'])[column].sum().reset_index()
        temp_df.rename(columns={column: 'pop_total'}, inplace=True)
        temp_df['period'] = period
        
        # 將新的資料框加入到 output_df 中
        output_df = pd.concat([output_df, temp_df], ignore_index=True)

# 按照COUNTYNAME、然後按period從小到大排序
output_df = output_df.sort_values(by=['COUNTYNAME', 'period'])

# 重新設定索引
output_df.reset_index(drop=True, inplace=True)

# # 將period的值轉換為文字格式
output_df['period'] = output_df['period'].astype(str)

# 儲存結果至新檔案
output_df.to_csv("output_dataset.csv", encoding="utf-8-sig", index=False)  # 將結果儲存為 CSV 檔案，如果需要其他格式，請適當地更改儲存函數
