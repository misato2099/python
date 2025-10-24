#42項指標大全
import ta
#import pandas as pd
def tech_indi_cal(df):
    # 在這裡使用 ta.add_all_ta_features 函式生成所有指標
    tech_indi_full = ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume", fillna=True)
    
    # 返回包含指標的資料框
    return tech_indi_full

def ma_cal(df):
    # 指數移動平均
    df['sma_3'] = ta.trend.SMAIndicator(df['Close'], window=3).sma_indicator()
    df['sma_5'] = ta.trend.SMAIndicator(df['Close'], window=5).sma_indicator()
    df['sma_20'] = ta.trend.SMAIndicator(df['Close'], window=20).sma_indicator()
    df['sma_90'] = ta.trend.SMAIndicator(df['Close'], window=90).sma_indicator()
    df['ema_5'] = ta.trend.EMAIndicator(df['Close'], window=5).ema_indicator()
    df['ema_10'] = ta.trend.EMAIndicator(df['Close'], window=10).ema_indicator()
    df['ema_20'] = ta.trend.EMAIndicator(df['Close'], window=20).ema_indicator()
    df['ema_30'] = ta.trend.EMAIndicator(df['Close'], window=30).ema_indicator()
    df['ema_60'] = ta.trend.EMAIndicator(df['Close'], window=60).ema_indicator()
    df['ema_90'] = ta.trend.EMAIndicator(df['Close'], window=90).ema_indicator()

    return df
###################################################################
###############################指標明細#############################
###################################################################

# **交易量（Volume）類**
# *資金流量指標（Money Flow Index，MFI）：結合價格和交易量，用於評估買賣壓力和超買或超賣的情況。
# 累積／派發指標（Accumulation/Distribution Index，ADI）：根據價格和交易量的關係，評估資金的流入和流出。
# 平衡量價指標（On-Balance Volume，OBV）：通過分析交易量的變動，判斷價格趨勢的強弱和买卖压力的平衡。
# ***蔡金資金流量指標（Chaikin Money Flow，CMF）：結合價格和交易量，用於測量買賣壓力和資金流入流出的強弱。(預設20天) = volume_cmf

# 力量指數（Force Index，FI）：根據價格變動和交易量，衡量買賣力量的強度。
# 動量指數（Ease of Movement，EoM，EMV）：根據價格變動和交易量，評估買賣力量和市場流動性。
# 成交量價格趨勢（Volume-price Trend，VPT）：通過分析成交量的變動，評估價格趨勢的強弱。
# *負成交量指數（Negative Volume Index，NVI）：根據成交量的變動，評估價格趨勢的強弱和買賣壓力。
# 加權平均價格（Volume Weighted Average Price，VWAP）：根據交易量加權的平均價格，評估價格水平。

# **波動性(Volatility)類：評估價格的變動幅度和市場的波動性**
# 平均真實範圍（Average True Range，ATR）：計算一段時間內的價格範圍，用於評估波動性。
# ***布林帶（Bollinger Bands，BB）：通過計算價格的標準差，形成上下兩個通道，用於衡量價格的波動性。(預設20天) 高於上軌 = volatility_bbhi、高於下軌 = volatility_bbli
# 凱特納通道（Keltner Channel，KC）：結合移動平均和價格範圍，用於觀察價格趨勢和波動性。
# 唐奇安通道（Donchian Channel，DC）：根據價格的最高值和最低值，形成上下兩個通道，用於觀察價格的突破和趨勢。
# 潰瘍指數（Ulcer Index，UI）：根據價格的回撤幅度，評估投資風險和市場情緒。

# **趨勢(Trend)類：評估價格的趨勢和方向**
# 簡單移動平均（Simple Moving Average，SMA）：計算一段時間內的價格平均值，用於觀察價格趨勢。一律平等(預設12)
# ***指數移動平均（Exponential Moving Average，EMA）：根據加權的平均計算價格，用於觀察價格趨勢。近重遠輕(預設14天)
# ???***加權移動平均（Weighted Moving Average，WMA）：根據加權的平均計算價格，用於觀察價格趨勢。近重遠輕(但較EMA平均)(預設9天)
# ***移動平均匯聚發散（Moving Average Convergence Divergence，MACD）：結合快速和慢速移動平均線，用於觀察價格趨勢的轉折點。(預設快12、慢26) = trend_macd
# 平均趨向指數（Average Directional Movement Index，ADX）：評估價格趨勢的強度和方向。
# 渦流指標（Vortex Indicator，VI）：根據價格的高低點和交易量，評估價格趨勢的強弱。
# TRIX（TRIX）：計算價格的平滑指數移動平均線，用於觀察價格趨勢的變化。
# 質量指數（Mass Index，MI）：根據價格範圍的變動，評估價格趨勢的轉折點。
# 商品通道指數（Commodity Channel Index，CCI）：根據價格的偏離程度，評估超買或超賣的情況。
# 去趋势价格振荡器（Detrended Price Oscillator，DPO）：去除趨勢後的價格變化，用於觀察價格的週期性變動。
# KST 振荡器（KST Oscillator，KST）：結合多個時間周期的移動平均線，用於觀察價格趨勢的變化。
# 一目均衡表（Ichimoku Kinkō Hyō，Ichimoku）：根據多個移動平均線和雲層，評估價格趨勢和支撐阻力位。
# 抛物轉向停損指标（Parabolic Stop And Reverse，Parabolic SAR）：根據價格趨勢的轉折點，提供停損和反向交易的參考。
# 斯夸夫趋势循环指标（Schaff Trend Cycle，STC）：結合移動平均和隨機指標，用於觀察價格趨勢的變化。

# **動量(Momentum)類：評估價格變動的速度和力量**
# ***相對強弱指數（Relative Strength Index，RSI）：根據價格變動的強度，評估超買或超賣的情況。(預設=14日) = momentum_rsi
# 隨機相對強弱指數（Stochastic RSI，SRSI）：根據相對強弱指數的變動，評估超買或超賣的情況。(即%K%D線)
# 真實強度指數（True strength index，TSI）：根據價格的變動和平滑指數移動平均線，評估超買或超賣的情況。
# ??***終極指數（Ultimate Oscillator，UO）：結合多個時間周期的相對強弱指數，用於評估超買或超賣的情況。短=7天(權4)、中=14天(權2)、長=28天(權1)
# 隨機指標（Stochastic Oscillator，SR）：根據價格的變動，評估超買或超賣的情況。
# 威廉指數（Williams %R，WR）：根據價格的變動，評估超買或超賣的情況。
# 驚人指標（Awesome Oscillator，AO）：根據移動平均線的交叉，評估價格趨勢的轉折點。
# 卡瑪自適應移動平均（Kaufman's Adaptive Moving Average，KAMA）：根據價格的變動，調整移動平均線的平滑度。
# 變動率（Rate of Change，ROC）：計算價格的變動率，用於評估價格趨勢的速度。
# 百分比價格振盪器（Percentage Price Oscillator，PPO）：計算移動平均線之間的百分比差異，用於觀察價格趨勢的變化。

# **其他：評估資產的收益和變化。**
# 每日收益（Daily Return，DR）
# 每日對數收益（Daily Log Return，DLR）
# 累積收益（Cumulative Return，CR）

###################################################################
###################################################################
###################################################################




