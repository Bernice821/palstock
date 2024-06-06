from init import db
from model import User, New, Stock, Figure
from flask import Flask, url_for, redirect, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import func
from init import create_app
from datetime import datetime
import csv
import os
import json


app = create_app()
CORS(app)

@app.route('/api/NewsStock',methods=['POST'])
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
    req = request.json
    stocks_num = req['StocksNum']
    stock_ids  = req['StocksID']
    time       = req['time']
    stock = []
    for i in range(stocks_num):
        data = db.session.execute(db.select(Stock).filter_by(id=stock_ids[i]).filter(func.date(Stock.time_stamp) == time).order_by(Stock.time_stamp.desc())).scalar()
        stock.append(data.index_obj_to_dict())
    return jsonify(stock)


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
    title = req['StocksName']
    time = req['time']
    datas = db.session.execute(db.select(Stock).filter_by(id=id).order_by(Stock.time_stamp.desc()).limit(time)).scalars()
    stocks_chart = []
    stock = {}
    for data in datas:
        stocks_chart.append(data.info_obj_to_dict())
    # stock['time'] = time
    stock['StockID'] = id
    stock['StockName'] = title
    stock['StockChart'] = stocks_chart
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


            
