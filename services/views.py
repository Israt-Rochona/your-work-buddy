from django.shortcuts import render

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
    return render (request,template_name='services/service.html')

def login(request):
    return render (request,template_name='services/login.html')