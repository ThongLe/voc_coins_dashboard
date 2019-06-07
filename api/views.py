from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Coin, MarketSummary
from .serializers import CoinSerializer
from .serializers import MarketSummarySerializer
from .tasks import store_coin_price


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all().order_by('name')
    serializer_class = CoinSerializer


class MarketSummaryViewSet(viewsets.ModelViewSet):
    queryset = MarketSummary.objects.all().order_by('-timestamp')
    serializer_class = MarketSummarySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            store_coin_price.delay(serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

