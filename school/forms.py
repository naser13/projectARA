from django.forms import ModelForm
from .models import School


class NewSchool(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'telephone']