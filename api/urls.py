from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'markets', views.MarketViewSet)
router.register(r'coins', views.CoinViewSet)
router.register(r'tickers', views.TicketViewSet)
router.register(r'query-tests', views.QueryTestsViewSet)


urlpatterns = router.urls

summary_urlpatterns = [
    url(r'^ma/', views.moving_average, name='ma'),
]

urlpatterns += [
    url(r'^summary/', include(summary_urlpatterns, namespace='summary')),
]