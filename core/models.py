from django.db import models

class Commodity(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    exchange = models.CharField(max_length=100)
    mic_code = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    timestamp = models.IntegerField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    previous_close = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    percent_change = models.DecimalField(max_digits=5, decimal_places=2)
    average_volume = models.BigIntegerField()
    is_market_open = models.BooleanField()

    # 52-week range data
    f_low = models.DecimalField(max_digits=10, decimal_places=2)
    f_high = models.DecimalField(max_digits=10, decimal_places=2)
    f_low_change = models.DecimalField(max_digits=10, decimal_places=2)
    f_high_change = models.DecimalField(max_digits=10, decimal_places=2)
    f_low_change_percent = models.DecimalField(max_digits=5, decimal_places=2)
    f_high_change_percent = models.DecimalField(max_digits=5, decimal_places=2)
    f_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name
