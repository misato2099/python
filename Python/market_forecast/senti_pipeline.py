from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertConfig
from simpletransformers.classification import ClassificationModel
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import torch
from scipy.stats import mode
from torch.nn.functional import softmax
import pandas as pd
import numpy as np
from tqdm import tqdm
import re
import jieba
import joblib


def sentiment_analysis_zh(df):

    sentiment_column = 'Sentiment_label'
    
    if sentiment_column not in df.columns:
        df[sentiment_column] = None
    
    # 篩選需要計算的資料列
    rows_to_calculate = df[df[sentiment_column].isnull()]
    
    if 'title' not in df.columns:
        return print('資料框中可能缺少 \'title\' 欄位')
    
    if rows_to_calculate.empty:
        print('情緒分析結果已經全部更新。')
        return df

    model = ClassificationModel("bert","D:\\****finbert_zh", use_cuda=False)

    # 提取需要分析的文本資料
    data_to_analyze = rows_to_calculate['title'].tolist()

    # 使用模型進行預測
    predictions, raw_outputs = model.predict(data_to_analyze)

    # 更新資料框中的 Sentiment_label 欄位
    df.loc[rows_to_calculate.index, sentiment_column] = predictions

    return df

###################################################################################################################


def senti_direction_zh(df):
    # 轉換日期格式為 'YYYY-mm-dd'
    df['source_date'] = pd.to_datetime(df['source_date'], format='%Y/%m/%d')

    # 獲取資料的日期範圍
    date_range = pd.date_range(start=df['source_date'].min(), end=df['source_date'].max(), freq='D')

    # 檢查日期範圍是否少於七天
    if len(date_range) < 7:
        recent_data = df
    else:
        current_date = pd.to_datetime('today').normalize()
        start_date = current_date - pd.DateOffset(days=6)
        recent_data = df[(df['source_date'] >= start_date) & (df['source_date'] <= current_date)]

    # 數算'1'和'0'的筆數
    total_count = len(recent_data['Sentiment_label'])
    count_pos = (recent_data['Sentiment_label'] == 1).sum()
    count_neg = (recent_data['Sentiment_label'] == 0).sum()
    positive_ratio = count_pos / total_count
    negative_ratio = count_neg / total_count

    if positive_ratio >= 0.7:
        trend = "正面"
    elif positive_ratio <= 0.3:
        trend = "負面"
    else:
        trend = "中性"
    
    return positive_ratio, negative_ratio, trend


###################################################################################################################


def sentiment_analysis_en(df, tokenizer, model):

    sentiment_columns = ['Positive_sentim', 'Negative_sentim', 'Neutral_sentim']

    if 'Sentiment_label' not in df.columns:
        df['Sentiment_label'] = None

    for column in sentiment_columns:
        if column not in df.columns:
            df[column] = None

    # 篩選需要計算的資料列
    rows_to_calculate = df[(df[sentiment_columns + ['Sentiment_label']].isnull().all(axis=1))]

    if rows_to_calculate.empty:
        print('情緒分析結果已經全部更新。')
        return df

    for i, row in tqdm(rows_to_calculate.iterrows(), total=rows_to_calculate.shape[0]):
        try:
            title = row['title']
        except:
            return print('資料框中可能缺少 \'title\' 欄位')

        # 預處理輸入片語
        input = tokenizer(title, padding=True, truncation=True, return_tensors='pt')
        
        # 進行推論
        output = model(**input)

        # 通過 softmax 層將模型輸出 logits 轉換為情感分數
        predictions = softmax(output.logits, dim=-1)
        
        # 將情感分數插入 dataframe 中的相應列
        for j, column in enumerate(sentiment_columns):
            df.at[i, column] = predictions[0][j].tolist()

        # 標註最高機率的情緒方向
        max_index = torch.argmax(predictions) # 根據你設定的情緒欄位名稱預序，0是第一欄，本情況就是'Positive_sentim'
        if max_index == 0:
            df.at[i, 'Sentiment_label'] = 1  # Positive_sentim 最高
        elif max_index == 1:
            df.at[i, 'Sentiment_label'] = -1  # Negative_sentim 最高(二元從-1改為0)
        else:
            df.at[i, 'Sentiment_label'] = 0  # Neutral_sentim 最高

    return df


###################################################################################################################


def senti_direction_en(df):
    # 轉換日期格式為 'YYYY-mm-dd'
    df['source_date'] = pd.to_datetime(df['source_date'], format='%Y-%m-%d')

    # 獲取資料的日期範圍
    date_range = pd.date_range(start=df['source_date'].min(), end=df['source_date'].max(), freq='D')

    # 檢查日期範圍是否少於七天
    if len(date_range) < 7:
        recent_data = df
    else:
        current_date = pd.to_datetime('today').normalize()
        start_date = current_date - pd.DateOffset(days=7)
        recent_data = df[(df['source_date'] >= start_date) & (df['source_date'] <= current_date)]

    # 數算 '1' 、 '0' 和 '-1' 的筆數(正負面可能要加權)
    count_pos = (recent_data['Sentiment_label'] == 1).sum() 
    count_neu = (recent_data['Sentiment_label'] == 0).sum()
    count_neg = (recent_data['Sentiment_label'] == -1).sum()

    pos_ratio = count_pos / (count_pos + count_neg)

    if pos_ratio >= 0.6:
        result = '正面'
    elif pos_ratio <= 0.4:
        result = '負面'
    else:
        result = '中性'

    # # 比較筆數並輸出結果
    # if count_pos > count_neu and count_pos > count_neg:
    #     result = '正面'
    # elif count_neg > count_neu and count_neg > count_pos:
    #     result = '負面'
    # else:
    #     result = '中性'

    # 回傳結果
    return count_pos, count_neu, count_neg, pos_ratio * 100, result
