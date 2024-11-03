from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
    print("home page request :", request)
    
    return HttpResponse("Hello World")

class AboutPageView(TemplateView):
    print("----------------about page request :")

    template_name = "about.html"