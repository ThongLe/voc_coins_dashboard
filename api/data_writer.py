from django.core.cache import cache


def write_coin(coin):
    coin.save()
    cache.set('coin:{}'.format(coin.code), coin)


def write_market(market):
    market.save()
    cache.set('market:{}'.format(market.code), market)


def write_ticker(ticker):
    market_code = ticker.market.code if hasattr(ticker, 'market') else ticker.get('market')
    sequence = ticker.sequence if hasattr(ticker, 'sequence') else ticker.get('sequence')
    cache.set('market:{}:date:{}'.format(market_code, sequence), ticker)


def write_incr_sequence(market_code):
    cache.incr('market:{}:sequence'.format(market_code))


def write_sequence(market_code, sequence):
    cache.set('market:{}:sequence'.format(market_code), sequence)