from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.http import JsonResponse

from .models import Coin, Market, Ticket
from .serializers import CoinSerializer
from .serializers import MarketSerializer
from .serializers import TicketSerializer
from .tasks import store_coin_price

from . import cacher


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all().order_by('code')
    serializer_class = CoinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                cacher.cache_coin(serializer.instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                None
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all().order_by('code')
    serializer_class = MarketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                cacher.cache_market(serializer.instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as ex:
                None
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-id')
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data['sequence'] = cacher.get_sequence(data['market'])
            store_coin_price.delay(data)

            cacher.cache_sequence(data['market'], data['sequence'] + 1)
            cacher.cache_ticket(data)
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def moving_average(request):
    market = request.GET.get('market')
    sequence = int(request.GET.get('sequence'))
    ma = int(request.GET.get('ma'))

    if None not in {market, sequence}:
        current_sequence = cacher.get_sequence(market)

        if current_sequence < sequence:
            return Response(status=status.HTTP_404_NOT_FOUND)

        sequences = list([current_sequence - _ for _ in range(ma)])
        tickets = cacher.get_tickets(market, sequences)

        total = sum(map(lambda _: _.price, tickets))
        return JsonResponse({'ma': total / ma})

    return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
