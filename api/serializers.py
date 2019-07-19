from rest_framework import serializers

from .models import Coin, Market, Ticker, QueryTest


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('code', 'name')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('code', 'coin', 'unit')


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('market', 'price', 'volumn', 'date', 'sequence')


class QueryTestSerializer(serializers.ModelSerializer):
    params = serializers.JSONField()

    class Meta:
        model = QueryTest
        fields = ['func', 'params', 'result', 'expected', 'created_at', 'passed']
