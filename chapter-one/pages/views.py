from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def homePageView(request):

    context = {
        "name": "Munna",
        "dept": "cse"
    }

    
    return TemplateResponse(request, "pages/home.html", context)


def aboutPageView(request):

    return render(request, "pages/about.html")


def contactPageView(request):
    context = {"name": "munna", "address": "Dhaka", "phone": "01773100924"}

    return JsonResponse(context)


def profilePageView(request, id):
    return JsonResponse({"name": "ifti", "id": id})