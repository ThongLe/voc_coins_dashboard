from celery.utils.log import get_task_logger
from coinsdashboard.celery import app

from .serializers import TicketSerializer


logger = get_task_logger(__name__)


@app.task
def store_coin_price(data):
    serializer = TicketSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
