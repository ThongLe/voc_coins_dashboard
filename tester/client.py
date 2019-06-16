import requests


def send_request(func):
    def wrapper(*args, **kwargs):
        method, url, data = func(*args, **kwargs)
        try:
            request_func = getattr(requests, method.lower())
            return request_func(url, data=data)
        except AttributeError:
            print "Method {} not found".format(method)
    return wrapper


@send_request
def get_coins(method='GET', url='http://localhost:8000/api/coins/', **kwargs):
    return method, url, kwargs.get('data')


@send_request
def send_ticket(method='POST', url='http://localhost:8000/api/tickers/', **kwargs):
    return method, url, kwargs.get('data')


@send_request
def send_query(method='GET', url='http://localhost:8000/api/query-tests/check_query/', **kwargs):
    return method, url, kwargs.get('data')


# send_ticket(data={
#     "market": "BTC-USDT",
#     "price": 12.0,
#     "volumn": 6.0,
#     "timestamp": "2019-02-01T01:00:00Z",
# })

#
# send_query(data={
#     "name": "1",
#     "params": "2",
#     "result": "3",
#     "expected": "4",
#     "passed": True
# })

# send_query(data={"name": "1", "params": "2", "expected": "c"})
