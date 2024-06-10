def test_home(client):
    res = client.get('/home')
    assert b'Hello, World!' in res.data

