from django.db import models
from school.models import School
from ara_test.values import Values


class HeadMaster(models.Model):
    first_name = models.CharField(Values.texts_fa.get('name'), max_length=80)
    last_name = models.CharField(Values.texts_fa.get('last_name'), max_length=80)
    national_ID = models.CharField(Values.texts_fa.get('national_ID'), max_length=10, unique=True)
    father_name = models.CharField(Values.texts_fa.get('father_name'), max_length=80, blank=True)
    school = models.OneToOneField(School)

    def __str__(self):
        return self.first_name + ' ' + self.last_name