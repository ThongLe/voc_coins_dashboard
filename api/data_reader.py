from django.core.cache import cache
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist

from .models import Coin
from .models import Market
from .models import Ticker


def read_coin(coin_code):
    try:
        coin = cache.get('coin:{}'.format(coin_code))
        coin = coin or Coin.objects.get(code=coin_code)
    except ObjectDoesNotExist:
        coin = None
    return coin


def read_market(market_code):
    try:
        market = cache.get('market:{}'.format(market_code))
        market = market or Market.objects.get(code=market_code)
    except ObjectDoesNotExist:
        market = None
    return market


def read_sequence(market_code):
    sequence = cache.get('market:{}:sequence'.format(market_code))
    sequence = sequence or Ticker\
        .objects\
        .filter(market__code=market_code)\
        .aggregate(Max('sequence'))\
        .get('sequence__max', 0)
    if sequence is not None:
        return sequence + 1
    return 0


def read_ticker(market_code, date):
    try:
        ticker = cache.get('market:{}:date:{}'.format(market_code, date))
        ticker = ticker or Ticker.objects.get(market__code=market_code, date=date)
    except ObjectDoesNotExist:
        ticker = None
    return ticker


def read_coins(coin_codes):
    keys = ['coin:{}'.format(coin_code) for coin_code in coin_codes]
    cached_coin_dicts = cache.get_many(keys)

    cached_coins = {}
    if cached_coin_dicts.__len__():
        cached_coins = {Coin(**coin_dict) for coin_dict in cached_coin_dicts.values()}

    missed_coin_codes = set(coin_codes) - set(cached_coin_dicts.keys())
    queried_coins = {}
    if missed_coin_codes.__len__():
        queried_coins = set(Coin.objects.filter(code__in=missed_coin_codes))

    return list(cached_coins | queried_coins)


def read_markets(market_codes):
    keys = ['market:{}'.format(market_code) for market_code in market_codes]
    cached_market_dicts = cache.get_many(keys)

    cached_markets = {}
    if cached_market_dicts.__len__():
        cached_markets = {Market(**market_dict) for market_dict in cached_market_dicts.values()}

    missed_market_codes = set(market_codes) - set(cached_market_dicts.keys())
    queried_markets = {}
    if missed_market_codes.__len__():
        queried_markets = set(Market.objects.filter(code__in=missed_market_codes))

    return list(cached_markets | queried_markets)


def read_tickets(market_code, dates):
    keys = ['market:{}:date:{}'.format(market_code, date) for date in dates]
    cached_ticker_dicts = cache.get_many(keys)

    cached_tickers = set([])
    if cached_ticker_dicts.__len__():
        cached_tickers = {Ticker(**ticker_dict) for ticker_dict in cached_ticker_dicts.values()}

    missed_ticker_codes = set(dates) - set(cached_ticker_dicts.keys())
    queried_tickers = {}
    if missed_ticker_codes.__len__():
        queried_tickers = set(Ticker.objects.filter(market=market_code, date__in=missed_ticker_codes))

    return list(cached_tickers | queried_tickers)
