from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

def homeView(request):
    return render(request, "posts/home.html", {"title": "you are right"})


class PostPageView(ListView):
    model = Post
    template_name = "posts/post.html"
    context_object_name = "post_list"

