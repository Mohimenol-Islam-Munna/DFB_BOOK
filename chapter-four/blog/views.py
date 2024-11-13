from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class BlogPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"


class BlogDetailPageView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"


class BlogCreateView(CreateView):
    model = Post
    template_name= "blog/create.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/create.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog_home")
