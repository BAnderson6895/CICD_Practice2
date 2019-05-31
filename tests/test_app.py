
from CICDPractice2.app import app


def test_get_page():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/')
    assert b'Hello World' in result.data

def test_get_bar():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/foo?bar=42')
    assert b'42' in result.data