from django.urls import path,re_path
from third_app import views

urlpatterns = [
    re_path(r'^$',views.AppleStore, name = 'AppleStore')
]
