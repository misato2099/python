import pandas as pd
import os

yearlist = ["year_1","year_N"]

filelist = []

openst = {"VAR": "1"}

i = 0

sourceFolderPath = os.path.join(os.path.dirname(__file__), 'merge')
for root, folders, files in os.walk(sourceFolderPath):
    for file in sorted(files):
        if file[0] != '.' and file[0] != '~' and file[:4] == 'KW':
            filePath = os.path.join(root, file)
            df = pd.read_csv(filePath, encoding='utf-8-sig', header=0)
            df[yearlist[i]] = df['column_N'].map(openst)
          
            # 儲存分檔
            savingFilePath = os.path.join(sourceFolderPath, file)
            df.to_csv(savingFilePath,
                      index=False, encoding='utf-8-sig')

            i += 1
