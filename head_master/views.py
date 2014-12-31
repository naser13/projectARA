from django.shortcuts import render, redirect
from .forms import NewHeadMaster
from school.forms import NewSchool
from address.forms import NewAddress


def new_headmaster(request):
    if request.method == 'POST':
        headmaster_form = NewHeadMaster(data=request.POST)
        school_form = NewSchool(data=request.POST)
        address_form = NewAddress(data=request.POST)
        if headmaster_form.is_valid() and school_form.is_valid() and address_form.is_valid():
            headmaster = headmaster_form.save(commit=False)
            school = school_form.save(commit=False)
            address = address_form.save()
            school.address = address
            school.save()
            headmaster.school = school
            headmaster.save()
            return redirect('home')
    else:
        headmaster_form = NewHeadMaster()
        address_form = NewAddress()
        school_form = NewSchool()
    return render(request, "new_headmaster.html",
                  {'form1': headmaster_form, 'form3': address_form, 'form2': school_form})
