from django.db import models
from address.models import Address
from ara_test.values import Values


class School(models.Model):
    name = models.CharField(Values.texts_fa.get('school_name'), max_length=200)
    telephone = models.CharField(Values.texts_fa.get('school_phone'), max_length=15, blank=True)
    address = models.OneToOneField(Address)

    def __str__(self):
        return self.name