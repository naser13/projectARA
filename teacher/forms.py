from django.forms import ModelForm, ValidationError
from .models import Teacher
from ara_test.values import Values


class NewTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'national_ID', 'father_name',
                  'academic_degree', 'field_of_study', 'university_name']

    def clean(self):
        if self.cleaned_data.get('national_ID') and \
                not self.cleaned_data.get('national_ID').isdigit():
            raise ValidationError(Values.texts_fa.get('national_ID_error'))
        return self.cleaned_data