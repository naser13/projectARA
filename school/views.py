from django.shortcuts import render, redirect
from school.forms import NewSchool
from address.forms import NewAddress


def new_school(request):
    if request.method == 'POST':
        address_form = NewAddress(data=request.POST)
        school_form = NewSchool(data=request.POST)
        if school_form.is_valid() and address_form.is_valid():
            school = school_form.save(commit=False)
            address = address_form.save()
            school.address = address
            school.save()
            back = request.GET.get('next', None)
            if back:
                return redirect(back)
            else:
                return redirect('home')
    else:
        address_form = NewAddress()
        school_form = NewSchool()
    return render(request, "new_school.html",
                  {'from': request.GET.get('from', None), 'form1': school_form, 'form2': address_form})
