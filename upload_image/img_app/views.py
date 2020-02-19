from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from img_app.forms import HotelForm
from img_app.models import Hotel

def hotel_img_method(request):
    if request.method == 'POST':
        form = HotelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return redirect('display_hotel_img')
    else:
        form = HotelForm()
    return render(request,'img_app/img_app.html',{'form':form})
def success(request):
    return HttpResponse('successfully uploaded')

def display_hotel_img(request):
    if request.method == 'GET':
        Hotels = Hotel.objects.all()
        datas = {'hotel_imgs':Hotels}
        return render(request,'img_app/display_hotel_img.html',datas)
