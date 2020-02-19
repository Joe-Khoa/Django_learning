from django.shortcuts import render
from django.http import HttpResponse
from third_app.models import Topic,WebPage, AccessRecord,User
from third_app.forms import NewUserForm
from django.core import validators
from django import forms
# from django import forms

def AppleStore(request):
    webPage_list = AccessRecord.objects.order_by('date')
    User_list = User.objects.order_by('first_name')
    data = {'title' : 'AppleStore',
            'header' : 'Welcome Store',
            'access_record' : webPage_list,
            'user_list' : User_list,
            }
    return render(request,'layouts/MasterLayout.html',context = data )

def index(request):
    webPage_list = AccessRecord.objects.order_by('date')
    User_list = User.objects.order_by('first_name')
    data = {'title' : 'Users',
            'header' : 'USER INFO',
            'access_record' : webPage_list,
            'user_list' : User_list,
            }
    return render(request,'layouts/uses.html',context = data )

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            print('import successfully!')
            return index(request)
        else:
            print('error : form invalid!')
    return render(request,'layouts/uses.html',{'form':form})
