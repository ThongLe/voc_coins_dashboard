import requests


r = requests.post(
    'http://localhost:8000/api/tickers/',
    data={
        "market": "BTC-USDT",
        "price": 12.0,
        "volumn": 6.0,
        "timestamp": "2019-02-01T01:00:00Z",
    }
)

print(r.status_code)