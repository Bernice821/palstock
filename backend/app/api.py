from flask import request, jsonify, Blueprint
from datetime import datetime, timedelta
from .init import db, create_app
from .model import New, Stock, Figure, Indicator
from .stock_calculation import calculate_indicators
import os
import json
import pandas as pd
import subprocess

api = Blueprint('api', __name__)

cur_dir = os.path.dirname(os.path.abspath(__file__))


@api.route('/api/newsStocks',methods=['POST'])
def news_stock():
    # insert_news()
    req = request.json
    news_num = req['newsNum']
    datas = db.session.execute(db.select(New).order_by(New.time_stamp.desc()).limit(news_num)).scalars()
    news = []
    for n in datas:
        news.append(n.obj_to_dict())
    return jsonify(news)

@api.route('/api/Market', methods=['POST'])
def market_page():
    req = request.get_json()

    start_tw = datetime.strptime(req['StartDate_Taiwan'], '%Y-%m-%d').replace(hour=0, minute=0, second=0)
    end_tw   = datetime.strptime(req['EndDate_Taiwan'], '%Y-%m-%d').replace(hour=23, minute=59, second=59)
    start_dj = datetime.strptime(req['StartDate_DJ'], '%Y-%m-%d').replace(hour=0, minute=0, second=0)
    end_dj   = datetime.strptime(req['EndDate_DJ'], '%Y-%m-%d').replace(hour=23, minute=59, second=59)

    tw_latest = db.session.execute(db.select(Figure).filter_by(name='加權指數').order_by(Figure.time_stamp.desc()).limit(2)).scalars().all()
    tw_today  = tw_latest[0].close
    tw_yesterday = tw_latest[1].close

    dj_latest = db.session.execute(db.select(Figure).filter_by(name='道瓊指數').order_by(Figure.time_stamp.desc()).limit(2)).scalars().all()
    dj_today  = dj_latest[0].close
    dj_yesterday = dj_latest[1].close

    indi_latest = db.session.execute(db.select(Indicator).order_by(Indicator.time_stamp.desc()).limit(1)).scalar()

    fig = {}

    fig['TaiwanPriceToday'] = tw_today
    fig['TaiwanPriceYesterday'] = tw_yesterday
    fig['DJPriceToday'] = dj_today
    fig['DJPriceYesterday'] = dj_yesterday
    fig['Indicators'] = indi_latest.score

    fig['TaiwanStocksChart'] = []
    fig['TaiwanVolume'] = []
    fig['DJStocksChart'] = []
    fig['IndicatorsHistory'] = []

    tw_datas = db.session.execute(db.select(Figure).filter(Figure.name == '加權指數', Figure.time_stamp >= start_tw, Figure.time_stamp <= end_tw).order_by(Figure.time_stamp.asc())).scalars().all()
    for f in tw_datas:
        time = f.time_stamp.strftime('%Y-%m-%d')

        stock_info = {}
        stock_info['x'] = time
        stock_info['y'] = [f.open, f.highest, f.lowest, f.close]
        fig['TaiwanStocksChart'].append(stock_info)

        vol_info = {}
        vol_info['x'] = time
        vol_info['y'] = f.volume
        fig['TaiwanVolume'].append(vol_info)
    
    dj_datas = db.session.execute(db.select(Figure).filter(Figure.name == '道瓊指數', Figure.time_stamp >= start_dj, Figure.time_stamp <= end_dj).order_by(Figure.time_stamp.asc())).scalars().all()
    for f in dj_datas:
        time = f.time_stamp.strftime('%Y-%m-%d')

        stock_info = {}
        stock_info['x'] = time
        stock_info['y'] = [f.open, f.highest, f.lowest, f.close]
        fig['DJStocksChart'].append(stock_info)

    indicator_datas = db.session.execute(db.select(Indicator).order_by(Indicator.time_stamp.desc()).limit(13)).scalars()
    for indicator in indicator_datas:
        time = indicator.time_stamp.strftime('%Y-%m')

        indicator_info = {}
        indicator_info['x'] = time
        indicator_info['y'] = indicator.score
        fig['IndicatorsHistory'].append(indicator_info)

    return jsonify(fig)

@api.route('/api/indexStocks', methods=['POST'])
def index_stocks():
    req        = request.get_json()
    stocks_num = req['StocksNum']
    stock_ids  = req['StocksID']
    time_str   = req['time'] #當天亦可包含至query結果內

    target_time = datetime.strptime(time_str, "%Y/%m/%d %H:%M:%S")
    target_time = target_time.replace(hour=23, minute=59, second=59)
    start_time  = target_time - timedelta(7)
    start_time  = start_time.replace(hour=0, minute=0, second=0)

    stocks = []
    for i in range(stocks_num):
        datas = db.session.execute(db.select(Stock).filter_by(id=stock_ids[i]).filter(Stock.time_stamp > start_time, Stock.time_stamp <= target_time).order_by(Stock.time_stamp.desc()).limit(7)).scalars()
        stock = {}
        stock['StocksChart'] = []
        for data in datas:
            stock['StocksTitle'] = data.name
            stock['StocksChart'].append(data.close)
        stocks.append(stock)
    print(stocks)
    return jsonify(stocks)


@api.route('/api/StrategyStock', methods=['POST'])
def strategy_stock():
    input_path  = os.path.join(cur_dir, '../backtest/buy_and_hold.json')
    py_path     = os.path.join(cur_dir, '../backtest/backtest.py')
    output_path  = os.path.join(cur_dir, '../backtest/output.json')

    data = request.get_json()
    with open(input_path, 'w') as f:
        json.dump(data, f)

    test_res = subprocess.run(['python3', py_path], capture_output=True, text=True)

    if test_res.returncode != 0:
        return jsonify({'Error': 'Backtest failed', 'Details':test_res.stderr}), 500
    
    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            output = json.load(f)
        return jsonify(output)
    else:
        return jsonify({'error': 'Output file not found'}), 500


@api.route('/api/StockInformation', methods=['POST'])
def stock_information():
    req = request.get_json()

    id = req['StocksID']
    name = req['Stockstitle']
    
    start_T = datetime.strptime(req['StartDate_T'] + " 00:00:00", "%Y-%m-%d %H:%M:%S")  #當天亦可包含至query結果內
    end_T = datetime.strptime(req['EndDate_T'] + " 23:59:59", "%Y-%m-%d %H:%M:%S")  
    start_P = datetime.strptime(req['StartDate_P'] + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    end_P = datetime.strptime(req['EndDate_P'] + " 23:59:59", "%Y-%m-%d %H:%M:%S")
    index = req['selectedIndex']


    #可能只有id或title

    if(id != ""):
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
    
    stk_key = ['k', 'd', 'j', 'dif', 'macd', 'dif-macd', 'rsi6', 'rsi12', 'rsi24']

    for key in stk_key:
        stock[key] = [{'x':x, 'y':y} for x, y, in zip( P_df['time_stamp'].to_list(), P_df[key.upper()].to_list())]

    return jsonify(stock)

