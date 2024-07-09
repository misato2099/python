import pandas as pd
import os

yearlist = ["open_09212", "open_09312", "open_09412", "open_09512", "open_09612", "open_09712", "open_09812",
            "open_09906", "open_09912", "open_10006", "open_10012", "open_10106", "open_10112", "open_10206",
            "open_10212", "open_10306", "open_10312", "open_10406", "open_10412", "open_10506", "open_10512",
            "open_10606", "open_10612", "open_10706", "open_10712", "open_10806", "open_10812", "open_10906",
            "open_10912", "open_11006"]

filelist = []

openst = {"營業中": "1"}

i = 0

sourceFolderPath = os.path.join(os.path.dirname(__file__), '合併檔')
for root, folders, files in os.walk(sourceFolderPath):
    for file in sorted(files):
        if file[0] != '.' and file[0] != '~' and file[:4] == 'BGMF':
            filePath = os.path.join(root, file)
            df = pd.read_csv(filePath, encoding='utf-8-sig', header=0)
            df[yearlist[i]] = df['營業狀況（營業中、停業中、停業以外之非營業中）'].map(openst)
          
            # 儲存分檔
            savingFilePath = os.path.join(sourceFolderPath, file)
            df.to_csv(savingFilePath,
                      index=False, encoding='utf-8-sig')

            i += 1