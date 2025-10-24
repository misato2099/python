import os
import pandas as pd
from datetime import datetime, timedelta
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from google.cloud import storage

# Google Cloud Storage 相關設定
bucket_name = "eg_bucket-1"
csv_file_tw = "news_tw.csv"
csv_file_us = 'news_us.csv'

# 設定ChromeDriver路徑
chrome_driver_path = '/usr/local/bin/chromedriver'

# def check_file_existence(csv_file_path):
#     # 初始化 Google Cloud Storage 客戶端
#     client = storage.Client()

#     # 獲取儲存桶
#     bucket = client.get_bucket(bucket_name)

#     # 檢查檔案是否存在
#     blob = bucket.blob(csv_file_path)
#     if blob.exists():
#         return True
#     else:
#         return False

# 檢查 Cloud Storage 中是否存在指定檔案

def download_file_from_gcs(csv_file_path):
    # 初始化 Google Cloud Storage 客戶端
    client = storage.Client()

    # 獲取儲存桶
    bucket = client.get_bucket(bucket_name)

    # 指定下載的檔案路徑和來源 blob 名稱
    source_blob_name = csv_file_path
    blob = bucket.blob(source_blob_name)

    # 指定下載的目的地檔案路徑
    destination_file_path = os.path.basename(csv_file_path)

    # 下載檔案至本地
    blob.download_to_filename(destination_file_path)

    print(f"檔案已成功從儲存桶 {bucket_name} 中的 {source_blob_name} 下載至本地檔案 {destination_file_path}。")


# Yahoo財經台灣
def crawler_tw():
    global csv_file_tw
    url1 = 'https://tw.finance.yahoo.com/tw-market'
    url2 = 'https://tw.finance.yahoo.com/news'

    def check_file_existence(bucket_name, file_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        return blob.exists()
    
    # 設定ChromeOptions
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 載入網頁
    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(url1)

    # 模擬滾動到最底
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 等待網頁更新
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 取得網頁內容
    html = driver.page_source

    # 解析 HTML 內容
    soup = BeautifulSoup(html, 'html.parser')

    # 找到包含title的元素，並獲取標題及source
    titles1 = soup.find_all('a', class_='Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')
    sources1 = soup.find_all('div', class_='C(#959595) Fz(13px) C($c-secondary-text)! D(ib) Mb(6px)')

    # 關閉瀏覽器
    driver.quit()

    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(url2)

    # 模擬滾動到最底
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 等待網頁更新
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 取得網頁內容
    html = driver.page_source

    # 解析 HTML 內容
    soup = BeautifulSoup(html, 'html.parser')

    # 找到包含title的元素，並獲取標題及source
    titles2 = soup.find_all('a', class_='Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')
    sources2 = soup.find_all('div', class_='C(#959595) Fz(13px) C($c-secondary-text)! D(ib) Mb(6px)')

    # 關閉瀏覽器
    driver.quit()

    # 建立資料框架
    if check_file_existence(bucket_name, csv_file_tw):
    # 如果 Cloud Storage 中已存在 "news_tw.csv" 檔案，則下載該檔案到本地
        download_file_from_gcs(csv_file_tw)
    else:
    # 如果 Cloud Storage 中不存在 "news_tw.csv" 檔案，則建立空的資料框架並儲存為 CSV 檔案
        empty_df = pd.DataFrame(columns=['crawl_date', 'source_date', 'title', 'source', 'source_time', 'Sentiment_label'])
        empty_df.to_csv(csv_file_tw, index=False, encoding='utf-8-sig')
    # if not os.path.exists(csv_file_tw):
    #     empty_df = pd.DataFrame(columns=['crawl_date', 'source_date', 'title', 'source', 'source_time', 'Sentiment_label'])
    #     empty_df.to_csv(csv_file_tw, index=False, encoding='utf-8-sig')
    
    df_tw = pd.read_csv(csv_file_tw, encoding='utf-8-sig')

    # 逐個獲取並添加爬取的資料至資料框架
    for title, source in zip(titles1, sources1):
        title_text = title.text.strip()
        source_text = source.text.strip()
        date = datetime.now().strftime('%Y/%m/%d %H:%M')

        # 分割「source」中的資料到「source_time」
        source_parts = source_text.split('•')
        if len(source_parts) > 1:
            source_text = source_parts[0].strip()
            source_time = source_parts[1].strip()
        else:
            source_text = source_parts[0].strip()  # 如果沒有 '•'，將整個 source_parts[0] 作為 source_text
            source_time = "1 秒前"  # 將沒有 '•' 的資料設置為 "1 秒前"

        # 添加資料至資料框架
        new_data = pd.DataFrame({'crawl_date': [date], 'title': [title_text], 'source': [source_text], 'source_time': [source_time]})
        df_tw = pd.concat([df_tw, new_data], ignore_index=True)

    for title, source in zip(titles2, sources2):
        title_text = title.text.strip()
        source_text = source.text.strip()
        date = datetime.now().strftime('%Y/%m/%d %H:%M')

        # 分割「source」中的資料到「source_date」
        source_parts = source_text.split('•')
        if len(source_parts) > 1:
            source_text = source_parts[0].strip()
            source_time = source_parts[1].strip()
        else:
            source_time = None

        # 添加資料至資料框架
        new_data = pd.DataFrame({'crawl_date': [date], 'title': [title_text], 'source': [source_text], 'source_time': [source_time]})
        df_tw = pd.concat([df_tw, new_data], ignore_index=True)

    # 將資料框架輸出為 CSV 檔案
    df_tw.to_csv(csv_file_tw, index=False, encoding='utf-8-sig')

    print(f'爬蟲資料已儲存至{csv_file_tw}檔案中。')

def source_date_tw(csvfile):
    global csv_file_tw
    df_tw = pd.read_csv(csvfile)

    # 逐行處理資料
    for index, row in df_tw.iterrows():
        crawl_date = datetime.strptime(row['crawl_date'], '%Y/%m/%d %H:%M')
        source_time = row['source_time']

        # 判斷source_time的類型
        if '秒' in source_time:
            sec = int(source_time.split(' ')[0])
            source_date = crawl_date - timedelta(seconds=sec)
        elif '小時' in source_time:
            hr = int(source_time.split(' ')[0])
            source_date = crawl_date - timedelta(hours=hr)
        elif '分鐘' in source_time:
            min = int(source_time.split(' ')[0])
            source_date = crawl_date - timedelta(minutes=min)
        elif source_time == '昨天':
            source_date = crawl_date - timedelta(days=1)
        elif source_time == '前天':
            source_date = crawl_date - timedelta(days=2)
        else:
            days_ago = int(source_time.replace('天前', ''))
            source_date = crawl_date - timedelta(days=days_ago)

        # 將計算得到的source_date填入「source_date」欄位
        df_tw.at[index, 'source_date'] = source_date.strftime('%Y/%m/%d')

    # 儲存處理後的資料至 CSV 檔案
    df_tw.to_csv(csvfile, index=False, encoding='utf-8-sig')
    # 回傳處理後的資料框
    return df_tw

def remove_symbols_tw(csvfile):
    global csv_file_tw
    df_tw = pd.read_csv(csvfile)

    # 逐行處理資料
    for index, row in df_tw.iterrows():
        title = row['title']
        if '【公告】' in title:
            df_tw = df_tw.drop(index)  # 刪除含有【公告】的列
        else:
            clean_title = re.sub(r'【.*?】|《.*?》', '', title)
            df_tw.at[index, 'title'] = clean_title

    # 檢查重複的title並保留最後一筆
    df_tw = df_tw.drop_duplicates(subset='title', keep='last')
    df_tw = df_tw[['crawl_date', 'source_date', 'title', 'source', 'source_time', 'Sentiment_label']]

    # 按舊至新重新排序
    df_tw = df_tw.sort_values('source_date')

    # 將日期欄位轉換為日期時間對象
    df_tw['source_date'] = pd.to_datetime(df_tw['source_date'])
    
    # 取得7天前的日期
    seven_days_ago = datetime.now() - timedelta(days=7)

    # 選擇日期大於7天前的行
    df_tw = df_tw[df_tw['source_date'] > seven_days_ago]
    
    # 儲存處理後的資料至 CSV 檔案
    df_tw.to_csv(csvfile, index=False, encoding='utf-8-sig')

    # 回傳處理後的資料框
    return df_tw

# Yahoo財經美國
def crawler_us():
    #clear_output(wait=True)
    global csv_file_us
    url1 = 'https://finance.yahoo.com/topic/stock-market-news/'
    url2 = 'https://finance.yahoo.com/topic/economic-news'

    def check_file_existence(bucket_name, file_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        return blob.exists()

    # 設定ChromeOptions
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 載入網頁
    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(url1)

    # 模擬滾動到最底
    temp_height = 0

    while True:
        driver.execute_script("window.scrollBy(0,1000)")

        time.sleep(2)

        check_height = driver.execute_script("return document.documentElement.scrollTop || window.pageOffset || document.body.scrollTop;")

        if check_height == temp_height:
            break
        temp_height = check_height
        #print(check_height)

    # 取得網頁內容
    html = driver.page_source

    # 解析 HTML 內容
    soup = BeautifulSoup(html, 'html.parser')

    # 找到包含title的元素，並獲取標題及source
    titles1 = soup.find_all('a', class_='js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')
    sources1 = soup.find_all('div', class_='C(#959595) Fz(11px) D(ib) Mb(6px)')

    # 關閉瀏覽器
    driver.quit()

    # driver = webdriver.Chrome("C:\\Users\\user\\anaconda3\\envs\\detector\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe",options=option) # WIN版
    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(url2)

    # 模擬滾動到最底
    temp_height = 0

    while True:
        driver.execute_script("window.scrollBy(0,1000)")

        time.sleep(2)

        check_height = driver.execute_script("return document.documentElement.scrollTop || window.pageOffset || document.body.scrollTop;")

        if check_height == temp_height:
            break
        temp_height = check_height
        #print(check_height)

    # 取得網頁內容
    html = driver.page_source

    # 解析 HTML 內容
    soup = BeautifulSoup(html, 'html.parser')

    # 找到包含title的元素，並獲取標題及source
    titles2 = soup.find_all('a', class_='js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')
    sources2 = soup.find_all('div', class_='C(#959595) Fz(11px) D(ib) Mb(6px)')

    # 關閉瀏覽器
    driver.quit()
    
    # 檢查檔案是否存在
    # 建立資料框架
    if check_file_existence(bucket_name, csv_file_us):
    # 如果 Cloud Storage 中已存在 "news_tw.csv" 檔案，則下載該檔案到本地
        download_file_from_gcs(csv_file_us)
    else:
    # 如果 Cloud Storage 中不存在 "news_tw.csv" 檔案，則建立空的資料框架並儲存為 CSV 檔案
        empty_df = pd.DataFrame(columns=['crawl_date', 'source_date', 'title', 'source', 'source_time', 'Sentiment_label', 'Positive_sentim', 'Negative_sentim', 'Neutral_sentim'])
        empty_df.to_csv(csv_file_us, index=False, encoding='utf-8-sig')
    df_us = pd.read_csv(csv_file_us, encoding='utf-8-sig')

    # 逐個獲取並添加爬取的資料至資料框架
    for title, source in zip(titles1, sources1):
        title_text = title.text.strip()
        source_text = source.text.strip()
        date = datetime.now().strftime('%Y/%m/%d %H:%M')

        # 分割「source」中的資料到「source_date」
        source_parts = source_text.split('•')
        if len(source_parts) > 1:
            source_text = source_parts[0].strip()
            source_time = source_parts[1].strip()
        else:
            source_text = source_parts[0].strip()  # 如果沒有 '•'，將整個 source_parts[0] 作為 source_text
            source_time = "1 second ago"  # 將沒有 '•' 的資料設置為 "1 second ago"

        # 添加資料至資料框架
        new_data = pd.DataFrame({'crawl_date': [date], 'title': [title_text], 'source': [source_text], 'source_time': [source_time]})
        df_us = pd.concat([df_us, new_data], ignore_index=True)
 
    for title, source in zip(titles2, sources2):
        title_text = title.text.strip()
        source_text = source.text.strip()
        date = datetime.now().strftime('%Y/%m/%d %H:%M')

        # 分割「source」中的資料到「source_date」
        source_parts = source_text.split('•')
        if len(source_parts) > 1:
            source_text = source_parts[0].strip()
            source_time = source_parts[1].strip()
        else:
            source_text = source_parts[0].strip()  # 如果沒有 '•'，將整個 source_parts[0] 作為 source_text
            source_time = "1 second ago"  # 將沒有 '•' 的資料設置為 "1 second ago"

        # 添加資料至資料框架
        new_data = pd.DataFrame({'crawl_date': [date], 'title': [title_text], 'source': [source_text], 'source_time': [source_time]})
        df_us = pd.concat([df_us, new_data], ignore_index=True)
         
    # 將資料框架輸出為 CSV 檔案
    df_us.to_csv(csv_file_us, index=False, encoding='utf-8-sig')

    print(f'爬蟲資料已儲存至{csv_file_us}檔案中。')

def source_date_us(csvfile):
    #clear_output(wait=True)
    global csv_file_us
    df_us = pd.read_csv(csvfile)

    # 逐行處理資料
    for index, row in df_us.iterrows():
        crawl_date = datetime.strptime(row['crawl_date'], '%Y/%m/%d %H:%M')
        source_time = row['source_time']
        source_time = source_time.strip()
        
        if 'second ago' in source_time or 'seconds ago' in source_time:
            sec = int(''.join(filter(str.isdigit, source_time)))
            source_date = crawl_date - timedelta(seconds=sec)
        elif 'minute ago' in source_time or 'minutes ago' in source_time:
            min = int(''.join(filter(str.isdigit, source_time)))
            source_date = crawl_date - timedelta(minutes=min)
        elif 'hour ago' in source_time or 'hours ago' in source_time:
            hr = int(''.join(filter(str.isdigit, source_time)))
            source_date = crawl_date - timedelta(hours=hr)
        elif source_time == 'yesterday':
            source_date = crawl_date - timedelta(days=1)
        # else:
        #     if source_time and source_time.strip() and source_time.strip().isdigit():
        #         days_ago = int(source_time)
        #         source_date = crawl_date - timedelta(days=days_ago)
        #     else:
        #         # 處理無效的 source_time 值的情況
        #         source_date = None  # 或者使用其他預設值或處理方式
        else:
            days_ago = int(''.join(filter(str.isdigit, source_time)))
            source_date = crawl_date - timedelta(days=days_ago)

        # 將計算得到的source_date填入「source_date」欄位
        df_us.at[index, 'source_date'] = source_date.strftime('%Y/%m/%d')

    # 檢查重複的title並保留最後一筆
    df_us['title'] = df_us['title'].str.replace("‘|’", "'", regex=True)
    df_us['title'] = df_us['title'].str.replace("—", "-", regex=True)
    df_us = df_us.drop_duplicates(subset='title', keep='last')
    #df.drop('source_time', axis=1, inplace=True)
    df_us = df_us[['crawl_date', 'source_date', 'title', 'source', 'source_time', 'Sentiment_label', 'Positive_sentim', 'Negative_sentim', 'Neutral_sentim']]

    # 按舊至新重新排序
    df_us = df_us.sort_values('source_date')

    # 將日期欄位轉換為日期時間對象
    df_us['source_date'] = pd.to_datetime(df_us['source_date'])

    # 取得7天前的日期
    seven_days_ago = datetime.now() - timedelta(days=7)

    # 選擇日期大於7天前的行
    df_us = df_us[df_us['source_date'] > seven_days_ago]
    
    # 儲存處理後的資料至 CSV 檔案
    df_us.to_csv(csvfile, index=False, encoding='utf-8-sig')
    # 回傳處理後的資料框
    return df_us


def upload_file_to_gcs(csv_file_path):
    # 初始化 Google Cloud Storage 客戶端
    client = storage.Client()

    # 獲取儲存桶
    bucket = client.get_bucket(bucket_name)

    # 指定上傳的檔案路徑和目的地 blob 名稱
    destination_blob_name = os.path.basename(csv_file_path)
    blob = bucket.blob(destination_blob_name)

    # 上傳檔案至 Google Cloud Storage
    blob.upload_from_filename(csv_file_path)

    print(f"檔案已成功上傳至儲存桶 {bucket_name} 中的 {destination_blob_name}。")

# 主程式
if __name__ == "__main__":
    # 設定 Chrome WebDriver 選項
    options = Options()
    options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 設定 Chrome WebDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    # 運行台灣新聞
    crawler_tw()
    df_tw = source_date_tw(csv_file_tw)
    df_tw = remove_symbols_tw(csv_file_tw)
    upload_file_to_gcs(csv_file_tw)
    
    # 運行美國新聞
    crawler_us()
    df_us = source_date_us(csv_file_us)
    upload_file_to_gcs(csv_file_us)
    
    # 關閉 Chrome WebDriver
    driver.quit()

