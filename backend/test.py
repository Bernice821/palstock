import pytest
from app.init import create_app




app = create_app()
app.config.update({
    'TESTING': True
})

client = app.test_client()

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
    datas = res.json

    print(type(datas['k'][0]['y']))

test_stock_information(client)