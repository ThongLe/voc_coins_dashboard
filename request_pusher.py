import requests


r = requests.post(
    'http://127.0.0.1:8000/api/market_summaries/',
    data={
        "name": "BTC-LTC",
        "high": 0.0135,
        "low": 0.012,
        "volumn": 3833.97619253,
        "timestamp": "2014-07-09T07:22:16.720000Z"}
)

print(r.status_code)