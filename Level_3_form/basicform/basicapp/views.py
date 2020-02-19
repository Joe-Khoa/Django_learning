from django.shortcuts import render
# from basicapp,models import
from . import forms
# Create your views here.

def index(request):
    data = {'success':''}
    return render(request,'basicapp/index.html',context= data)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # pass
            print('validation success!')
            a = form.cleaned_data
            print('NAME: '+ a['name'])
            print('EMAIL: '+ a['email'])
            print('TEXT: '+ a['text'])
            # form.save(commit =True)
            s ='validation is successfull!'
            print(type(a))
            print('\n','#'*20)
            for i, x in enumerate(a):
                print(i,':',x )
            print('\n','#'*20)
            data = {'success' : s}
            print(data['success'])
            # form.save()
            return render(request,'basicapp/index.html',context= data)
        else:
            print('ERROR: invalid form!')
    return render(request,'basicapp/form_page.html',{'form' : form})
