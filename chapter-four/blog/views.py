from django.views.generic import ListView, DetailView
from .models import Post

class BlogPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"


class BlogDetailPageView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"