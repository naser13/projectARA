from django.forms import ModelForm
from .models import Teacher


class NewTeacher(ModelForm):
    class Meta:
        model = Teacher