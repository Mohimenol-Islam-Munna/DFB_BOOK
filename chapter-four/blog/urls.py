from django.urls import path
from .views import BlogPageView, BlogDetailPageView

urlpatterns = [
    path("<int:pk>", BlogDetailPageView.as_view(), name="blog_detail"),
    path("", BlogPageView.as_view(), name="blog_home"),
]