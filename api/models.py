from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Coin(TimeStampedModel):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)


class MarketSummary(TimeStampedModel):
    name = models.CharField(max_length=128)
    high = models.FloatField()
    low = models.FloatField()
    volumn = models.FloatField()
    timestamp = models.DateTimeField()
