from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'coins', views.CoinViewSet)
router.register(r'market_summaries', views.MarketSummaryViewSet)