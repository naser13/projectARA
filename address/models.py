from django.db import models


class Address(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    avenue = models.CharField(max_length=200, blank=True)
    alley = models.CharField(max_length=200, blank=True)
    more = models.TextField(blank=True)

    def __str__(self):
        return self.city + ' ' + self.street