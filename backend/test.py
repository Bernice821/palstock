import yfinance as yf
import pandas as pd

df = pd.read_csv('./crawl/stocks_datas/stock_2024_6_11.csv')

id_list = df['證券代號'].to_list()
print(id_list)


for i in range(0, len(id_list), 100):
    ticker = id_list[i]
    stock = yf.Ticker(ticker+'.TW')
    start_date = '2023-06-14'
    end_date = '2024-06-14'
    history = stock.history(start=start_date, end=end_date)
    history['ID'] = ticker
    print(history)



# for idx, row in history.iterrows():
#     print(f"Index: {idx}")
#     print(f"Row: \n{row}")

