from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse
from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)


def url(request):
    uri = request.build_absolute_uri()
    url = request.build_absolute_uri('?')
    print(uri)
    print(url)

# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse(" USE CBVIEWs ARE COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # template_name = 'basic_app/school_list.html' # the school_list auto

################ SCHOOL CRUD ################

class SchoolDetailView(DetailView):     # retrieve _ get data
    context_object_name = 'school_detail'
    model = models.School
    # template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

################ SCHOOL CRUD ################

class StudentCreateView(CreateView,View,):
    fields = ('name','age','school')
    model = models.Student
    print('#'*20,'#'*20)
    # print
    #
    # url(request)

    # the rule url(regex=r'^user/(?P<username>\w{1,50})/$', view='views.profile_page')
    # a in incoming request for http://domain/user/thaiyoshi/?message=Hi



    # def profile_page(request, username=None):
    #     user = User.objects.get(username=username)
    #     message = request.GET.get('message')
    #     print(user)
    #     print(message)

    success_url = reverse_lazy('basic_app:list')
