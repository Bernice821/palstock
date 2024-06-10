from app.init import create_app

app = create_app()
app.config.update({
        'TESTING': True
    })

def test_newsStocks(client):
    input = {
        "newsNum" : 7
    }
    res = client.post('/api/newsStocks', json=input)
    assert res.status_code == 200
    print(res.get_json())

client = app.test_client()
test_newsStocks(client)



