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

def provider_detail(request , id):
    pro= Provider.objects.get(pk=id)
    c = {
        'provider':pro,
    }
    return render(request, template_name='services\provider_details.html',context=c)

def login(request):
    return render (request,template_name='services/login.html')


def receiver(request):
    pro= consumer.objects.all()
    c = {
        'consumer':pro,
    }
    return render(request, template_name='services\service_receiver.html',context=c)

def receiver_detail(request , id) :
    pro= consumer.objects.get(pk=id)
    c = {
        'consumer':pro,
    }
    return render(request, template_name='services\consumer_detail.html',context=c)