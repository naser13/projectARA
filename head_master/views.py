from django.shortcuts import render, redirect
from .forms import NewHeadMaster
from school.forms import NewSchool
from address.forms import NewAddress
from user.forms import RegistrationForm


def new_headmaster(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)
        headmaster_form = NewHeadMaster(data=request.POST)
        school_form = NewSchool(data=request.POST)
        address_form = NewAddress(data=request.POST)
        if registration_form.is_valid() and \
                headmaster_form.is_valid() and \
                school_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            headmaster = headmaster_form.save(commit=False)
            school = school_form.save(commit=False)
            address = address_form.save()
            school.address = address
            school.save()
            headmaster.school = school
            headmaster.user = user
            headmaster.save()
            return redirect('home')
    else:
        registration_form = RegistrationForm()
        headmaster_form = NewHeadMaster()
        address_form = NewAddress()
        school_form = NewSchool()
    return render(request, "new_headmaster.html",
                  {'form': registration_form,
                   'form1': headmaster_form,
                   'form3': address_form,
                   'form2': school_form})
