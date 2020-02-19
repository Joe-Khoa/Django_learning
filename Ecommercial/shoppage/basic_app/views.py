from django.shortcuts import render
from basic_app import views

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')
def base(request):
    return render(request,'basic_app/base.html')
def about(request):
    return render(request,'basic_app/about.html')
def contact(request):
    return render(request,'basic_app/contact.html')
def products(request):
    return render(request,'basic_app/products.html')
def login(request):
    return render(request,'basic_app/login.html')
def faqs(request):
    return render(request,'basic_app/faq.html')
def preview(request):
    return render(request,'basic_app/preview.html')
def cart(request):
    return render(request,'basic_app/shopping_cart.html')
