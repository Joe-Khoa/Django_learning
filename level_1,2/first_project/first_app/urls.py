from django.urls import re_path,path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    path('home',views.first_home),
    re_path(r'^$',views.index,name = 'index'),
]
