from django.urls import path
from .views import BlogPageView, BlogDetailPageView, BlogCreateView

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>", BlogDetailPageView.as_view(), name="blog_detail"),
    path("", BlogPageView.as_view(), name="blog_home"),
]