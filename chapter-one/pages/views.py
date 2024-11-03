from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from django.views.generic import TemplateView
=======
from django.template.response import TemplateResponse
>>>>>>> 74c72c099d8869338ebbe664d640e1da213497f1

def homePageView(request):

    context = {
        "name": "Munna",
        "dept": "cse",
        "stacks": ["js", "ts", "py", "go"],
        "frameworks": [{"name": "react js", "type": "frontend"}, {"name": "next js", "type": "frontend"},{"name": "express js", "type": "backend"},{"name": "django", "type": "backend"}]
    }

    
<<<<<<< HEAD
    return HttpResponse("Hello World")

class AboutPageView(TemplateView):
    print("----------------about page request :")

    template_name = "about.html"
=======
    return TemplateResponse(request, "pages/home.html", context)


def aboutPageView(request):

    return render(request, "pages/about.html")


def contactPageView(request):
    context = {"name": "munna", "address": "Dhaka", "phone": "01773100924"}

    return JsonResponse(context)


def profilePageView(request, id):
    return JsonResponse({"name": "ifti", "id": id})
>>>>>>> 74c72c099d8869338ebbe664d640e1da213497f1
