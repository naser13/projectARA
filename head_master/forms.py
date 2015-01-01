from django.forms import ModelForm, forms
from .models import HeadMaster
from ara_test.values import Values


class NewHeadMaster(ModelForm):
    class Meta:
        model = HeadMaster
        fields = ['first_name', 'last_name', 'national_ID', 'father_name']

    def clean(self):
        if self.cleaned_data.get('national_ID') and not self.cleaned_data.get('national_ID').isdigit():
            raise forms.ValidationError(Values.texts_fa.get('national_ID_error'))
        return self.cleaned_data