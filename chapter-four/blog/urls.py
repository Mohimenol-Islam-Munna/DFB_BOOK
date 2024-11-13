from django.urls import path
from .views import BlogPageView, BlogDetailPageView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="blog_delete"),
    path("update/<int:pk>", BlogUpdateView.as_view(), name="blog_update"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>", BlogDetailPageView.as_view(), name="blog_detail"),
    path("", BlogPageView.as_view(), name="blog_home"),
]