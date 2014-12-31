from django.db import models
from school.models import School


class HeadMaster(models.Model):
    first_name = models.CharField('نام', max_length=80)
    last_name = models.CharField('نام خانوادگی', max_length=80)
    national_ID = models.CharField('کد ملی', max_length=10, unique=True)
    father_name = models.CharField('نام پدر', max_length=80, blank=True)
    school = models.OneToOneField(School)

    def __str__(self):
        return self.first_name + ' ' + self.last_name