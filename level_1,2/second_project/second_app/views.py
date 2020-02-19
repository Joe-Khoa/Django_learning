from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = { 'val' : 'MasterLayouts.html view', 'list' : ['list-temp','data'], }
    return render(request,'layouts/MasterLayout.html',context = data)
# Create your views here.
def help(request):
    return HttpResponse('Help page')
