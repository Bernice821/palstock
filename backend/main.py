from app.init import db
from app.model import New, Stock, Figure, Indicator
from flask import request, jsonify, Blueprint
from flask_cors import CORS
from app.init import create_app
from app.stock_calculation import calculate_indicators
from datetime import datetime
import os
import yfinance as yf
import pandas as pd

app = create_app()
CORS(app)

cur_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/historyStock')
def history_stock():
    data = yf.download('2330'+'.TW', start='2024-04-01', end='2024-05-31')
    data['ID'] = '2330'
    data['Name'] = '台積電'
    for idx, row in data.iterrows():
        time = idx.to_pydatetime()
        stock = Stock(id=row['ID'], name=row['Name'], volume=row['Volume'], trans_amt=0, 
                    open=row['Open'], close=row['Close'], highest=row['High'], lowest=row['Low'], 
                    change=0, trans_num=0, time_stamp = time)
        db.session.add(stock)
    db.session.commit()

    return jsonify({'Status': 'success'})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12000)