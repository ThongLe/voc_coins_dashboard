from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Coin(TimeStampedModel):
    code = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.code


class Market(TimeStampedModel):
    code = models.CharField(max_length=32, primary_key=True)
    coin = models.ForeignKey(Coin, related_name='markets')
    unit = models.ForeignKey(Coin, related_name='base_markets')

    def __str__(self):
        return self.code

    @property
    def coin_code(self):
        return self.coin

    @property
    def unit_code(self):
        return self.unit

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.code = '{}-{}'.format(self.coin.code, self.unit.code)
        super(self.__class__, self).save()


class Ticket(TimeStampedModel):
    market = models.ForeignKey(Market, related_name='tickets')
    price = models.FloatField()
    volumn = models.FloatField()
    timestamp = models.DateTimeField()
    sequence = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.market, self.sequence)
