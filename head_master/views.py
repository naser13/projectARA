from django.shortcuts import render, redirect
from .forms import NewHeadMaster


def new_headmaster(request):
    if request.method == 'POST':
        headmaster_form = NewHeadMaster(data=request.POST)
        if headmaster_form.is_valid():
            headmaster = headmaster_form.save()
            return redirect('new_school', headmaster=headmaster)
    else:
        headmaster_form = NewHeadMaster()
    return render(request, "new_headmaster.html", {'form': headmaster_form})
