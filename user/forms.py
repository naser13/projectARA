from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ara_test.values import Values


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = Values.texts_fa.get('username')
        self.fields['username'].help_text = ''
        self.fields['email'].label = Values.texts_fa.get('email')
        self.fields['password1'].label = Values.texts_fa.get('password1')
        self.fields['password2'].label = Values.texts_fa.get('password2')
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user