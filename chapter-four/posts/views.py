from django.shortcuts import render

def homeView(request):
    return render(request, "posts/home.html", {"title": "you are right"})
