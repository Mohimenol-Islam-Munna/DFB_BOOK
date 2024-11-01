from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def homePageView(request):

    context = {
        "name": "Munna",
        "dept": "cse",
        "stacks": ["js", "ts", "py", "go"],
        "frameworks": [{"name": "react js", "type": "frontend"}, {"name": "next js", "type": "frontend"},{"name": "express js", "type": "backend"},{"name": "django", "type": "backend"}]
    }

    
    return TemplateResponse(request, "pages/home.html", context)


def aboutPageView(request):

    return render(request, "pages/about.html")


def contactPageView(request):
    context = {"name": "munna", "address": "Dhaka", "phone": "01773100924"}

    return JsonResponse(context)


def profilePageView(request, id):
    return JsonResponse({"name": "ifti", "id": id})