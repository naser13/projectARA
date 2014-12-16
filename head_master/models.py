from django.db import models
from school.models import School


class HeadMaster(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    national_ID = models.CharField(max_length=10, unique=True)
    father_name = models.CharField(max_length=80)
    school = models.OneToOneField(School)

    def __str__(self):
        return self.first_name + ' ' + self.last_name