from django.forms import ModelForm, forms
from .models import School
from ara_test.values import Values


class NewSchool(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'telephone']

    def clean(self):
        if self.cleaned_data.get('telephone') and not self.cleaned_data.get('telephone').isdigit():
            raise forms.ValidationError(Values.texts_fa.get('telephone_error'))
        return self.cleaned_data