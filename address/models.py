from django.db import models
from ara_test.values import Values


class Address(models.Model):
    province = models.CharField(Values.texts_fa.get('province'), max_length=3, choices=Values.provinces)
    city = models.CharField(Values.texts_fa.get('city'), max_length=100)
    more = models.TextField(Values.texts_fa.get('address'), blank=True)

    def __str__(self):
        return self.city