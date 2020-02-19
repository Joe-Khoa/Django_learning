from basic_app import views
from django.conf.urls import url

app_name = 'basic_app'

urlpatterns = [
    url(r'base/$',views.base),
    url(r'index/$',views.index,name = 'index'),
    url(r'about/$',views.about,name = 'about'),
    url(r'contact/$',views.contact,name = 'contact'),
    url(r'products/$',views.products,name = 'products'),
    url(r'login/$',views.login,name = 'login'),
    url(r'faqs/$',views.faqs,name = 'faqs'),
    url(r'preview/$',views.preview,name = 'preview'),
    url(r'cart/$',views.cart,name = 'cart'),

]
