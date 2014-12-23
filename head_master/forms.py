from django.forms import ModelForm
from .models import HeadMaster


class NewHeadMaster(ModelForm):
    class Meta:
        model = HeadMaster
        # fields = ['first_name', 'last_name', 'national_ID', 'father_name']