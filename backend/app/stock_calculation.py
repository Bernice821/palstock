import pandas as pd

def calculate_ema(prices, days):
    return prices.ewm(span=days, adjust=False).mean()

def calculate_macd(data, short=12, long=26, signal=9):
    short_ema = calculate_ema(data['close'], short)
    long_ema = calculate_ema(data['close'], long)
    dif = short_ema - long_ema
    macd = calculate_ema(dif, signal)
    dif_macd = dif - macd
    return dif, macd, dif_macd

def calculate_rsi(data, period=5):
    delta = data['close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_kdj(data, period=9):
    data['Low_Min'] = data['lowest'].rolling(window=period).min()
    data['High_Max'] = data['highest'].rolling(window=period).max()
    data['RSV'] = (data['close'] - data['Low_Min']) / (data['High_Max'] - data['Low_Min']) * 100

    data['K'] = data['RSV'].ewm(com=2, adjust=False).mean()
    data['D'] = data['K'].ewm(com=2, adjust=False).mean()
    data['J'] = 3 * data['K'] - 2 * data['D']


def calculate_indicators(P_df):
    P_df['DIF'], P_df['MACD'], P_df['DIF-MACD'] = calculate_macd(P_df)
    P_df['RSI6'] = calculate_rsi(P_df, 6)
    P_df['RSI12'] = calculate_rsi(P_df, 12)
    P_df['RSI24'] = calculate_rsi(P_df, 24)
    calculate_kdj(P_df)
    