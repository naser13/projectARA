from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    national_ID = models.CharField(max_length=10, unique=True)
    father_name = models.CharField(max_length=80)
    degrees = (
        ('Bs', 'لیسانس'),
        ('Ms', 'فوق لیسانس'),
    )
    academic_degree = models.CharField(max_length=2, choices=degrees, default='Bs')

    def __str__(self):
        return self.first_name + ' ' + self.last_name