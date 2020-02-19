from django.urls import re_path,path
from django.conf.urls import url
from second_app import views

urlpatterns = [
    path('help',views.help,name = 'help' ),
]
