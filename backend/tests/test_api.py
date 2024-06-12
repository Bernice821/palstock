def test_home(client):
    res = client.get('/home')
    assert b'Hello, World!' in res.data

def test_news_stocks(client):
    input = {
        "newsNum" : 7
    }
    res = client.post('/api/newsStocks', json=input)
    assert res.status_code == 200

    datas = res.json
    assert len(datas) == input['newsNum']

    for data in datas:
        assert 'ImgUrl' in data and data['ImgUrl'].startswith('https://')
        assert 'Time' in data
        assert 'Title' in data
        assert 'Url' in data and data['Url'].startswith('https://')

        from datetime import datetime
        time = datetime.strptime(data['Time'], '%Y-%m-%d')
        assert isinstance(time, datetime)

        assert isinstance(data['Title'], str) and len(data['Title']) > 0

def test_strategy_stock(client):   
    input = {
        "TimePeriods": 0,
        "StartYear": 2021,
        "EndYear": 2023,
        "FirstMonth": 1,
        "LastMonth": 12,
        "IncludeYTD": 0,
        "initialAmount": 200000,
        "CashFlows": "Contribute fixed amount",
        "ContributionAmount": 10000,
        "ContributionFrequency": "Annually/Quarterly/Monthly",
        "Rebalancing": "None/Annually/Semi-Annually/Quarterly/Monthly",
        "ReinvestDividends": 0,
        "DisplayIncome": 0,
        "Benchmark": 1,
        "Portfolios": [
            {
                "StockID": "2330.TW",
                "part": [30, 20, 0]
            },
            {
                "StockID": "0050.TW",
                "part": [50, 40, 60]
            },
            {
                "StockID": "006208.TW",
                "part"   : [20, 40, 40]
            }
        ]
    }

    res = client.post('/api/StrategyStock', json=input)
    assert res.status_code == 200

    datas = res.json
    
    assert datas['Message'] == 'Success'
    assert len(datas['ReturnData']) == len(input["Portfolios"][0]["part"])

    for porf in datas['ReturnData']:
        
        assert isinstance(porf['Benchmark'], float)
        assert isinstance(porf['BestYear'], float)
        assert isinstance(porf['CAGR'], float)
        assert isinstance(porf['FinalBalance'], float)
        assert isinstance(porf['MIRR'], float)
        assert isinstance(porf['Max.Drawdown'], float)
        assert isinstance(porf['Portfolio'], float)
        assert isinstance(porf['SharpeRatio'], float)
        assert isinstance(porf['SortioRatio'], float)
        assert isinstance(porf['Stdev'], float)
        assert isinstance(porf['TWRR'], float)
        assert isinstance(porf['WorstYear'], float)
        assert isinstance(porf['title'], str)

def test_market(client):
    input = {
        "StartDate_Taiwan": "2024-06-06", 
        "EndDate_Taiwan": "2024-06-11",
        "StartDate_DJ": "2024-06-06", 
        "EndDate_DJ": "2024-06-11"
    }

    res = client.post('/api/Market', json=input)
    assert res.status_code == 200

    datas = res.json
    assert isinstance(datas['DJPriceToday'], float)
    assert isinstance(datas['DJPriceYesterday'], float)
    assert isinstance(datas['TaiwanPriceToday'], float)
    assert isinstance(datas['TaiwanPriceYesterday'], float)
    assert isinstance(datas['Indicators'], int)
    assert isinstance(datas['DJStocksChart'], list)
    assert isinstance(datas['TaiwanStocksChart'], list)
    assert isinstance(datas['IndicatorsHistory'], list)
    assert isinstance(datas['TaiwanVolume'], list)

    for item in datas['DJStocksChart']:
        assert "x" in item
        assert "y" in item
        assert isinstance(item["x"], str)
        assert isinstance(item["y"], list)
        assert len(item["y"]) == 4

    for item in datas['TaiwanStocksChart']:
        assert "x" in item
        assert "y" in item
        assert isinstance(item["x"], str)
        assert isinstance(item["y"], list)
        assert len(item["y"]) == 4
        
    for item in datas['TaiwanVolume']:
        assert "x" in item
        assert "y" in item
        assert isinstance(item["x"], str)
        assert isinstance(item["y"], float)

    for item in datas['IndicatorsHistory']:
        assert "x" in item
        assert "y" in item
        assert isinstance(item["x"], str)
        assert isinstance(item["y"], int)

def test_index_stocks(client):
    input = {
        "StocksNum": 3,
        "StocksID": ["0050", "2330", "00940"],
        "time": "2024/06/11 00:00:00"
    }

    res = client.post('/api/indexStocks', json=input)
    assert res.status_code == 200

    datas = res.json
    assert len(datas) == input['StocksNum']

    for data in datas:
        assert isinstance(data['StocksChart'], list)
        for ele in data['StocksChart']:
            assert isinstance(ele, int)
        assert isinstance(data['StocksTitle'], str)

def test_stock_information(client):
    input = {
        "StocksID" : "2330",
        "Stockstitle": "台積電",
        "StartDate_T": "2024-05-01", 
        "EndDate_T": "2024-06-11",
        "StartDate_P": "2024-05-01", 
        "EndDate_P": "2024-06-11",
        "selectedIndex": "kdj"
    }

    res = client.post('/api/StockInformation', json=input)
    assert res.status_code == 200

    datas = res.json
    assert datas['StocksID'] == input['StocksID']
    assert datas['Stockstitle'] == input['Stockstitle']

    assert isinstance(datas['StockPrice'], list)
    for data in datas['StockPrice']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], list) and len(data['y']) == 4

    assert isinstance(datas['Volume'], list)
    for data in datas['Volume']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], int)


    assert isinstance(datas['k'], list)
    for data in datas['k']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)


    assert isinstance(datas['d'], list)
    for data in datas['d']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['j'], list)
    for data in datas['j']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['macd'], list)
    for data in datas['macd']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['dif'], list)
    for data in datas['dif']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['dif-macd'], list)
    for data in datas['dif-macd']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['rsi6'], list)
    for data in datas['rsi6']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)

    assert isinstance(datas['rsi12'], list)
    for data in datas['rsi12']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)
    
    assert isinstance(datas['rsi24'], list)
    for data in datas['rsi24']:
        assert isinstance(data['x'], str)
        assert isinstance(data['y'], float)
