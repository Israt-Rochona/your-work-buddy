from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from.models import *

# Create your views here.

def home(request):
    return render (request,template_name='services/home.html')

def signup(request):
    return render (request,template_name='services/signup.html')

def about_us(request):
    return render (request,template_name='services/About_us.html')

def get_help(request):
    return render (request,template_name='services/help.html')

def service(request):
<<<<<<< HEAD
    service=Service.objects.all()
    context = {
        'service':service,
    }
    return render (request,template_name='services\service.html',context=context)

def provider(request):
    pro= Provider.objects.all()
    c = {
        'provider':pro,
    }
    return render(request, template_name='services\provider.html',context=c)


=======
    return render (request,template_name='services/service.html')

def login(request):
    return render (request,template_name='services/login.html')
>>>>>>> 87cf173125d8819fd0f69d01c2507f1240138cc1
