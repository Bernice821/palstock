from datetime import datetime

def test_home(client):
    res = client.get('/home')
    assert b'Hello, World!' in res.data

def test_newsStocks(client):
    input = {
        "newsNum" : 7
    }
    res = client.post('/api/newsStocks', json=input)
    assert res.status_code == 200

    datas = res.get_json()
    assert len(datas) == 7

    for data in datas:
        assert 'ImgUrl' in data
        assert 'Time' in data
        assert 'Title' in data
        assert 'Url' in data

        assert data['ImgUrl'].startswith('https://')

        assert data['Url'].startswith('https://')

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

    datas = res.get_json()
    
    assert datas['Message'] == 'Success'
    assert len(datas['ReturnData']) == len(input["Portfolios"][0]["part"])

    for porf in datas['ReturnData']:
        
        assert 'Benchmark' in porf and isinstance(porf['Benchmark'], float)
        assert 'BestYear' in porf and isinstance(porf['BestYear'], float)
        assert 'CAGR' in porf and isinstance(porf['CAGR'], float)
        assert 'FinalBalance' in porf and isinstance(porf['FinalBalance'], float)
        assert 'MIRR' in porf and isinstance(porf['MIRR'], float)
        assert 'Max.Drawdown' in porf and isinstance(porf['Max.Drawdown'], float)
        assert 'Portfolio' in porf and isinstance(porf['Portfolio'], float)
        assert 'SharpeRatio' in porf and isinstance(porf['SharpeRatio'], float)
        assert 'SortioRatio' in porf and isinstance(porf['SortioRatio'], float)
        assert 'Stdev' in porf and isinstance(porf['Stdev'], float)
        assert 'TWRR' in porf and isinstance(porf['TWRR'], float)
        assert 'WorstYear' in porf and isinstance(porf['WorstYear'], float)
        assert 'title' in porf and isinstance(porf['title'], str)

