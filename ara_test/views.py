from django.shortcuts import render


def ara_home(request):
    return render(request, "home.html")