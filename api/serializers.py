from rest_framework import serializers

from .models import MarketSummary, Coin


class CoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coin
        fields = ('name', 'code')


class MarketSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketSummary
        fields = ('name', 'high', 'low', 'volumn', 'timestamp')
