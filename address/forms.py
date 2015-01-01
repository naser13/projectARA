from django.forms import ModelForm
from .models import Address


class NewAddress(ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'more']