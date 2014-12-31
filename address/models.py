from django.db import models
from .values import Values


class Address(models.Model):
    province = models.CharField('استان', max_length=3, choices=Values.provinces)
    city = models.CharField('شهرستان', max_length=100)
    more = models.TextField('آدرس دقیق', blank=True)

    def __str__(self):
        return self.city + ' ' + self.street