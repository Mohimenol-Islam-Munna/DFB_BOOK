from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    print("home page request :", request)
    
    return HttpResponse("Hello World")