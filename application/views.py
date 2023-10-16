from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'application/HomePage.html');

def postProperty(request):
    return render(request, 'application/postProperty.html');

def propertyinquiry(request):
    return render(request, 'application/property inquiry.html');


def login(request):
    return render(request, 'application/login.html');


def residential(request):
    return render(request, 'application/residential.html');


def commercial(request):
    return render(request, 'application/commercial.html');

