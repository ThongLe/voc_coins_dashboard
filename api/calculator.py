from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response

import pendulum

from . import data_reader as dtr


func_dict = {}


def register(func):
    func_dict[func.__name__] = func

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@register
def moving_average(market_code='', days=0, date=pendulum.today(), *args, **kwargs):
    if days <= 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ticker = dtr.read_ticker(market_code, date)

    if ticker is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    dates_range = range(1, days)
    dates_range.reverse()
    dates = [date - timedelta(days=_) for _ in dates_range]
    tickers = dtr.read_tickets(market_code, dates) + [ticker]

    if tickers.__len__() < days:
        return Response(status=status.HTTP_404_NOT_FOUND)

    total_price = sum(map(lambda t: t.price, tickers))
    return total_price * 1. / days


@register
def minimum(market_code='', days=0, date=pendulum.today(), *args, **kwargs):
    if days <= 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ticker = dtr.read_ticker(market_code, date)

    if ticker is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    dates_range = range(1, days)
    dates_range.reverse()
    dates = [date - timedelta(days=_) for _ in dates_range]
    tickers = dtr.read_tickets(market_code, dates) + [ticker]

    if tickers.__len__() < days:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return min(map(lambda t: t.price, tickers))


@register
def maximum(market_code='', days=0, date=pendulum.today(), *args, **kwargs):
    if days <= 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ticker = dtr.read_ticker(market_code, date)

    if ticker is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    dates_range = range(1, days)
    dates_range.reverse()
    dates = [date - timedelta(days=_) for _ in dates_range]
    tickers = dtr.read_tickets(market_code, dates) + [ticker]

    if tickers.__len__() < days:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return max(map(lambda t: t.price, tickers))


def compute(*args, **kwargs):
    params = kwargs.get('params')
    params['date'] = pendulum.parse(params['date']).date()
    params['days'] = int(params['days'])
    return func_dict[kwargs.get('func')](**params)

