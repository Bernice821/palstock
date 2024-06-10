from flask import  jsonify, Blueprint
from datetime import datetime
from .init import db
from .model import New, Stock, Figure, Indicator
import csv
import os
import subprocess

database = Blueprint('database', __name__)

cur_dir = os.path.dirname(os.path.abspath(__file__))


@database.route('/db/GetAndInsertNews')
def get_news():
    crawler_path  = os.path.join(cur_dir, '../crawl/news_with_pic.py')
    res           = subprocess.run(['python3', crawler_path], text=True)
    
    if res.returncode != 0:
        return jsonify({'Error': 'Crwaler failed', 'Details':res.stderr}), 500
    
    return insert_news()


def insert_news():
    cur_time      = datetime.now()
    output_path   = os.path.join(cur_dir, f'../crawl/news_datas/news_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv')
    with open(output_path, 'r') as file:
        reader = csv.DictReader(file)
        news = []
        for new in reader:
            news.append(new)
    for n in news:
        new = New(title=n['title'], url=n['url'], src=n['src'], time_stamp=n['date'], pic_url=n['pic_url'])
        db.session.add(new)
    db.session.commit()

    return jsonify({'Success': 'News inserted!'}), 200


@database.route('/db/GetAndInsertStocks')
def get_stocks():
    crawler_path  = os.path.join(cur_dir, '../crawl/stock_crawl.py')
    res           = subprocess.run(['python3', crawler_path], text=True)
    
    if res.returncode != 0:
        return jsonify({'Error': 'Crwaler failed', 'Details':res.stderr}), 500
    
    return insert_stocks()

def insert_stocks():
    cur_time      = datetime.now()
    output_path   = os.path.join(cur_dir, f'../crawl/stocks_datas/stock_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv')
    with open(output_path, 'r') as file:
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
                    change=s['漲跌價差'], trans_num=s['成交筆數'], time_stamp = cur_time)
        db.session.add(stock)
    db.session.commit()

    return jsonify({'Success': 'Stocks inserted!'}), 200

@database.route('/db/GetAndInsertFigures')
def get_figures():
    crawler_path  = os.path.join(cur_dir, '../crawl/figure_crawl.py')
    res           = subprocess.run(['python3', crawler_path], text=True)
    
    if res.returncode != 0:
        return jsonify({'Error': 'Crwaler failed', 'Details':res.stderr}), 500

    return insert_figures()

def insert_figures():
    cur_time = datetime.now()
    output_path = os.path.join(cur_dir, f'../crawl/figures_datas/figures_data_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv')
    
    with open(output_path, 'r') as file:
        reader = csv.DictReader(file)
        figs = []
        for fig in reader:
            figs.append(fig)
    for f in figs:
        fig = Figure(name=f['指標名稱'], volume=f['成交量(億)'], open=f['開盤'], close=f['收盤'], highest=f['最高'], lowest=f['最低'], time_stamp=cur_time)
        db.session.add(fig)
    db.session.commit()

    return jsonify({'Success': 'Figures inserted!'}), 200

@database.route('/db/GetAndInsertIndicators')
def get_indicators():
    crawler_path  = os.path.join(cur_dir, '../crawl/business_indicators.py')
    res           = subprocess.run(['python3', crawler_path], text=True)
    
    if res.returncode != 0:
        return jsonify({'Error': 'Crwaler failed', 'Details':res.stderr}), 500
    return insert_indicators()

def insert_indicators():
    cur_time = datetime.now()
    output_path = os.path.join(cur_dir, f'../crawl/indicators_datas/indicators_datas_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv')

    with open(output_path, 'r') as file:
        reader = csv.DictReader(file)
        indicators = []
        for indi in reader:
            indicators.append(indi)
    for i in indicators:
        indicator = Indicator(time_stamp=datetime.strptime(i['date'], '%Y-%m'), score=i['score'])
        db.session.add(indicator)
    db.session.commit()
    
    return jsonify({'Success': 'Figures inserted!'}), 200
