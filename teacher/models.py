from django.db import models
from ara_test.values import Values
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(Values.texts_fa.get('name'), max_length=80)
    last_name = models.CharField(Values.texts_fa.get('last_name'), max_length=80)
    national_ID = models.CharField(Values.texts_fa.get('national_ID'), max_length=10, unique=True)
    father_name = models.CharField(Values.texts_fa.get('father_name'), max_length=80, blank=True)
    degrees = (
        ('Dip', 'دیپلم'),
        ('Bs', 'لیسانس'),
        ('Ms', 'فوق لیسانس'),
        ('PHD', 'دکتری')
    )
    academic_degree = models.CharField(Values.texts_fa.get('academic_degree'),
                                       max_length=3, choices=degrees, default='Dip')
    field_of_study = models.CharField(Values.texts_fa.get('field_of_study'), max_length=80, blank=True)
    university_name = models.CharField(Values.texts_fa.get('university_name'), max_length=80, blank=True)
    favorites = (
        ('Literature', 'ادبیات'),
        ('Arabic', 'عربی'),
        ('Religious', 'معارف'),
        ('English', 'زبان انگلیسی'),
        ('Maths', 'ریاضیات'),
        ('Physics', 'فیزیک'),
        ('chemistry', 'شیمی'),
        ('Biology', 'زیست شناسی'),
        ('Geology', 'زمین شناسی'),
        ('Social science', 'علوم اجتماعی'),
        ('Gym', 'ورزش'),
    )
    favorite_fields = models.CharField(max_length=15, choices=favorites)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.first_name + ' ' + self.last_name