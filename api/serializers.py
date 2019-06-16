from rest_framework import serializers

from .models import Coin, Market, Ticket, QueryTest


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('code', 'name')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('code', 'coin', 'unit')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('market', 'price', 'volumn', 'timestamp', 'sequence')


class QueryTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryTest
        fields = ['name', 'params', 'result', 'expected', 'created_at', 'passed']
