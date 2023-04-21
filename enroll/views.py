from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User

# This function will add Item and Show all items.
def add_show(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = UserForm()
    else:
        # will simply generate form without post data
        fm = UserForm()    
        # for fetching data
    stud = User.objects.all().values()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# this function will edit data
def update_data(request, id):
    pi = User.objects.get(pk = id)
    fm = UserForm(request.POST, instance=pi)
    if fm.is_valid():
        fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = UserForm(instance=pi) 
       
    return render(request, "enroll/updatestudent.html", {'form':fm})

# this function will delete item
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')