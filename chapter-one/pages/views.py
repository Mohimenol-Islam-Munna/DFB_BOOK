from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def homePageView(request):
    print("home page request.")
    
    return HttpResponse("Hello World")


def aboutPageView(request):

    return render(request, "pages/about.html")


def contactPageView(request):
    context = {"name": "munna", "address": "Dhaka", "phone": "01773100924"}

    return JsonResponse(context)