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
