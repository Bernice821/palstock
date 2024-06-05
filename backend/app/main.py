from init import db
from model import New, Stock, Figure
from flask import render_template, request, jsonify
from flask_cors import CORS
from init import create_app
from datetime import datetime, timedelta
from stock_calculation import calculate_indicators
import csv
import os
import json
import pandas as pd

app = create_app()
CORS(app)

@app.route('/api/newsStocks',methods=['POST'])
def news_stock():
    # insert_news()
    req = request.json
    news_num = req['newsNum']
    datas = db.session.execute(db.select(New).order_by(New.time_stamp.desc()).limit(news_num)).scalars()
    news = []
    for n in datas:
        news.append(n.obj_to_dict())
    return jsonify(news)


@app.route('/api/indexStocks', methods=['POST'])
def index_stocks():
    req        = request.get_json()
    stocks_num = req['StocksNum']
    stock_ids  = req['StocksID']
    time_str   = req['time'] + " 23:59:59" #當天亦可包含至query結果內

    target_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    start_time  = target_time - timedelta(7)

    stocks = []
    for i in range(stocks_num):
        datas = db.session.execute(db.select(Stock).filter_by(id=stock_ids[i]).filter(Stock.time_stamp > start_time, Stock.time_stamp <= target_time).order_by(Stock.time_stamp.desc()).limit(7)).scalars()
        stock = {}
        stock['StocksChart'] = []
        for data in datas:
            stock['StocksTitle'] = data.name
            stock['StocksChart'].append(data.close)
        stocks.append(stock)
    return jsonify(stocks)


@app.route('/api/StrategyStock', methods=['POST'])
def strategy_stock():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path  = os.path.join(current_dir, '../backtest/output.json')
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/api/StockInformation', methods=['POST'])
def stock_information():
    # insert_stocks()
    req = request.get_json()

    id = req['StocksID']
    name = req['Stockstitle']
    
    start_T = datetime.strptime(req['StartDate_T'] + " 00:00:00", "%Y-%m-%d %H:%M:%S")  #當天亦可包含至query結果內
    end_T = datetime.strptime(req['EndDate_T'] + " 23:59:59", "%Y-%m-%d %H:%M:%S")  
    start_P = req['StartDate_P'] + " 00:00:00"
    end_P = req['EndDate_P'] + " 23:59:59"
    index = req['selectedIndex']


    #可能只有id或title

    if(id != None):
        latest_datas = db.session.execute(db.select(Stock).filter(Stock.id==id).order_by(Stock.time_stamp.desc()).limit(2)).scalars().all()
        T_datas = db.session.execute(db.select(Stock).filter(Stock.time_stamp >= start_T, Stock.time_stamp <= end_T, Stock.id==id)).scalars().all()
        P_datas = db.session.execute(db.select(Stock).filter(Stock.time_stamp >= start_P, Stock.time_stamp <= end_P, Stock.id==id)).scalars().all()
    else:
        latest_datas = db.session.execute(db.select(Stock).filter(Stock.name==name).order_by(Stock.time_stamp.desc()).limit(2)).scalars().all()
        T_datas = db.session.execute(db.select(Stock).filter(Stock.time_stamp >= start_T, Stock.time_stamp <= end_T, Stock.name==name)).scalars().all()
        P_datas = db.session.execute(db.select(Stock).filter(Stock.time_stamp >= start_P, Stock.time_stamp <= end_P, Stock.name==name)).scalars().all()

    
    today_price = latest_datas[0].close
    yesterday_price = latest_datas[1].close
    stock = {}

    

    stock['StockPrice'] = []
    stock['Volume'] = []
    stock['priceToday'] = today_price
    stock['priceYesterday'] = yesterday_price

    for data in T_datas:
        stock['Stockstitle'] = data.name
        stock['StocksID'] = data.id

        price_info = {}
        price_info['x'] = data.time_stamp.strftime('%Y-%m-%d')
        price_info['y'] = [data.open, data.highest, data.lowest, data.close]
        stock['StockPrice'].append(price_info)

        vol_info  = {}
        vol_info['x'] = data.time_stamp.strftime('%Y-%m-%d')
        vol_info['y'] = data.volume
        stock['Volume'].append(vol_info)
    

    data_lst = [
        data.obj_to_dict() for data in P_datas
    ]


    
    P_df = pd.DataFrame(data_lst)
    calculate_indicators(P_df)
    
    stock['k'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['K'].to_list())]
    stock['d'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['D'].to_list())]
    stock['j'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['J'].to_list())]
    stock['dif'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['DIF'].to_list())]
    stock['macd'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['MACD'].to_list())]
    stock['dif-macd'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['DIF-MACD'].to_list())]
    stock['rsi6'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['RSI6'].to_list())]
    stock['rsi12'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['RSI12'].to_list())]
    stock['rsi24'] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df['RSI24'].to_list())]
    return jsonify(stock)




    
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/news')
def show_news():
    insert_news()
    news = db.session.execute(db.select(New).order_by(New.time_stamp.desc())).scalars()
    # news = db.session.execute(select(New).order_by(func.random())).first() #隨機挑選新聞
    return render_template('list_news.html', news=news)

def insert_news():
    with open('./crawl/news.csv', 'r') as file:
        reader = csv.DictReader(file)
        news = []
        for new in reader:
            news.append(new)
    for n in news:
        new = New(title=n['title'], url=n['url'], src=n['src'], time_stamp=n['date'], pic_url=n['pic_url'])
        db.session.add(new)
    db.session.commit()

def delete_news():
    news = db.session.execute(db.select(New)).scalars()
    for n in news:
        db.session.delete(n)
    db.session.commit()

@app.route('/stocks')
def show_stocks():
    insert_stocks()
    stocks = db.session.execute(db.select(Stock)).scalars()
    # delete_stocks()
    return render_template('list_stocks.html', stocks=stocks)

def insert_stocks():
    with open('./crawl/stocks.csv', 'r') as file:
        reader = csv.DictReader(file)
        stocks = []
        for stock in reader:
            stocks.append(stock)
    for s in stocks:
        for key, val in s.items():
            if val == "":
                s[key] = 0
        stock = Stock(id=s['證券代號'], name=s['證券名稱'], volume=s['成交股數'], trans_amt=s['成交金額'], 
                    open=s['開盤價'], close=s['收盤價'], highest=s['最高價'], lowest=s['最低價'], 
                    change=s['漲跌價差'], trans_num=s['成交筆數'])
        db.session.add(stock)
    db.session.commit()


def delete_stocks():
    stocks = db.session.execute(db.select(Stock)).scalars()
    for s in stocks:
        db.session.delete(s)
    db.session.commit()

@app.route('/figures')
def insert_figures():
    with open('./crawl/figure.csv', 'r') as file:
        reader = csv.DictReader(file)
        figs = []
        for fig in reader:
            figs.append(fig)
    for f in figs:
        fig = Figure(name=f['name'], volume=f['volume'], open=f['open'], close=f['close'], highest=f['highest'], lowest=f['lowest'])
        db.session.add(fig)
    db.session.commit()
        




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12000)