from django.shortcuts import render,redirect
from .forms import NewTeacher
from ara_test.views import ara_home


def new_teacher(request):
    if request.method == 'POST':
        form = NewTeacher(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewTeacher()
    return render(request, "new_teacher.html", {'form': form})
