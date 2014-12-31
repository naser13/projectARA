from django.db import models
from address.models import Address


class School(models.Model):
    name = models.CharField('نام مدرسه', max_length=200)
    telephone = models.CharField('تلفن', max_length=15, blank=True)
    address = models.OneToOneField(Address)

    def __str__(self):
        return self.name