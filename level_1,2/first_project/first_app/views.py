from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . import forms
# from forms import FormName

# def index(request):
#     my_dict= {"variable" : "Hello I am from view.py",
#                 "view_array" : ['blue', 'gray', 'white' ],
#                 }
#     return render(request,'index.html',context= my_dict)


def index(request):
    Acc_list = AccessRecord.objects.order_by('date')

    data = {'web_list': Acc_list,
    }
    # return HttpResponse("")
    return render(request,'index.html',context=data)

def first_home(request):
    return HttpResponse("""response of the first_home
    <br>
    <pre> property
    """)
# Create your views here.
def formpage(request):
    form = forms.FormName()
    # check post_sent?
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('validation succeeded!')
            var = form.cleaned_data
            # print('Name : '+var['name'])
            print('Email : '+var['email'])
            # print('text : '+var['text'])
            form.save()
            return render(request,'index.html',{'success':'imported successfully'})

        else:
            print('\n','*'*30)
            print('#'*50,'form is invalid!','#'*50)
            print('\n','*'*30)
    return render(request,'formpage.html',{'form': form})
