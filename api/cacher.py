from django.core.cache import cache
from django.db.models import Max

from .models import Coin
from .models import Market
from .models import Ticker


def cache_coin(coin):
    cache.set('coin:{}'.format(coin.code), coin)


def cache_market(market):
    cache.set('market:{}'.format(market.code), market)


def cache_ticket(ticket):
    market_code = ticket.market.code if hasattr(ticket, 'market') else ticket.get('market')
    sequence = ticket.sequence if hasattr(ticket, 'sequence') else ticket.get('sequence')
    cache.set('market:{}:ticket:{}'.format(market_code, sequence), ticket)


def cache_sequence(market_code, sequence):
    cache.set('market:{}:sequence'.format(market_code), sequence)


def get_coin(coin_code):
    coin = cache.get('coin:{}'.format(coin_code))
    if coin is None:
        coin = Coin.objects.get(code=coin_code)
    return coin


def get_market(market_code):
    market = cache.get('market:{}'.format(market_code))
    if market is None:
        market = Market.objects.get(code=market_code)
    return market


def get_sequence(market_code):
    sequence = cache.get('market:{}:sequence'.format(market_code))
    if sequence is None:
        sequence = \
            Ticker\
            .objects\
            .filter(market__code=market_code)\
            .aggregate(Max('sequence'))\
            .get('sequence__max', 0)
    return sequence


def get_ticket(market_code, sequence):
    ticket = cache.get('market:{}:ticket:{}'.format(market_code, sequence))
    if ticket is None:
        ticket = Ticker.objects.get(market__code=market_code, sequence=sequence)
    return ticket


def get_tickets(market_code, sequences):
    keys = ['market:{}:ticket:{}'.format(market_code, sequence) for sequence in sequences]
    cached_tickets = cache.get_many(keys)
    if cached_tickets.__len__() == sequences.__len__():
        return cached_tickets

    db_tickets = Ticker.objects.filter(market__code=market_code, sequence__in=sequences)

    tickets = [None] * sequences.__len__()

    for ticket in cached_tickets:
        index = sequences.index(ticket['sequence'])
        tickets[index] = ticket

    for ticket in db_tickets:
        index = sequences.index(ticket.sequence)
        tickets[index] = ticket

    return tickets


