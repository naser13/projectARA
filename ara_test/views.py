from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from  django.core.urlresolvers import reverse_lazy


def ara_home(request):
    return render(request, "home.html")

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('home')