from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import JsonResponse

from .models import Coin
from .models import Market
from .models import Ticket
from .models import QueryTest

from .serializers import CoinSerializer
from .serializers import MarketSerializer
from .serializers import TicketSerializer
from .serializers import QueryTestSerializer
from .tasks import store_coin_price

from . import cacher
from . import forms


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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().select_related('coin'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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


class QueryTestsViewSet(viewsets.ModelViewSet):
    queryset = QueryTest.objects.all().order_by('id')
    serializer_class = QueryTestSerializer

    @action(detail=False, methods=['GET'])
    def check_query(self, request):
        query_test_form = forms.QueryTestForm(request.GET)
        if query_test_form.is_valid():
            result = 'b'
            if result != query_test_form.cleaned_data['expected']:
                query_test = QueryTest(result=result, passed=False, **query_test_form.cleaned_data)
                query_test.save()

                serializer = self.get_serializer(query_test)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)