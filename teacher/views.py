from django.shortcuts import render, redirect
from .forms import NewTeacher
from user.forms import RegistrationForm


def new_teacher(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)
        teacher_form = NewTeacher(data=request.POST)
        if registration_form.is_valid() and teacher_form.is_valid():
            user = registration_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('home')
    else:
        registration_form = RegistrationForm()
        teacher_form = NewTeacher()
    return render(request, "new_teacher.html",
                  {'form': registration_form, 'form1': teacher_form})