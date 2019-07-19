from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Coin
from .models import Market
from .models import Ticker
from .models import QueryTest

from .serializers import CoinSerializer
from .serializers import MarketSerializer
from .serializers import TickerSerializer
from .serializers import QueryTestSerializer
from .tasks import store_coin_price

from . import data_reader as dtr
from . import data_writer as dtw
from . import forms

from . import calculator


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all().order_by('code')
    serializer_class = CoinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                coin = Coin(**serializer.validated_data)
                dtw.write_coin(coin)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                None
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data':serializer.data})


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all().order_by('code')
    serializer_class = MarketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                market = Market(**serializer.validated_data)
                dtw.write_market(market)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as ex:
                None
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().select_related('coin'))
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all().order_by('-id')
    serializer_class = TickerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data['sequence'] = dtr.read_sequence(data['market'])
            store_coin_price.delay(data)

            dtw.write_sequence(data['market'], data['sequence'] + 1)
            dtw.write_ticker(data)
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


# def moving_average(request):
#     market = request.GET.get('market')
#     sequence = int(request.GET.get('sequence'))
#     ma = int(request.GET.get('ma'))
#
#
#     if None not in {market, sequence}:
#         # current_sequence = cacher.get_sequence(market)
#         #
#         # if current_sequence < sequence:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         #
#         # sequences = list([current_sequence - _ for _ in range(ma)])
#         # tickets = cacher.get_tickets(market, sequences)
#         #
#         # total = sum(map(lambda _: _.price, tickets))
#
#         _market = None
#         _days = None
#         _date = None
#
#         ma = calculator.moving_average(_market, _days, _date)
#
#         return JsonResponse({'ma': ma})
#
#     return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class QueryTestsViewSet(viewsets.ModelViewSet):
    queryset = QueryTest.objects.all().order_by('id')
    serializer_class = QueryTestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})

    @action(detail=False, methods=['POST'])
    def check_query(self, request):
        query_test_form = forms.QueryTestForm(request.data)
        if query_test_form.is_valid():
            result = calculator.compute(**query_test_form.data)

            if isinstance(result, Response):
                return result

            if result != float(query_test_form.cleaned_data['expected']):
                query_test = QueryTest(result=result, passed=False, **query_test_form.data)
                query_test.save()

                serializer = self.get_serializer(query_test)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)