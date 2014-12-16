from django.shortcuts import render,redirect
from .forms import NewHeadMaster
from school.forms import NewSchool


def new_headmaster(request):
    if request.method == 'POST':
        headmaster_form = NewHeadMaster(data=request.POST)
        school_form = NewSchool(data=request.POST)
        if school_form.is_valid() and headmaster_form.is_valid():
            school = school_form.save()
            headmaster = headmaster_form.save(commit=False)
            headmaster.school = school
            headmaster.save()
            return redirect('home')
    else:
        headmaster_form = NewHeadMaster()
        school_form = NewSchool()
    return render(request, "new_headmaster.html", {'form1': headmaster_form, 'form2': school_form})
