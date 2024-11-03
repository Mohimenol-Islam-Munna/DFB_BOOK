from django.urls import path
from .views import homePageView, aboutPageView, contactPageView, profilePageView


urlpatterns = [
    path("", homePageView, name="home"),
    path("about", aboutPageView, name="about"),
    path("contact", contactPageView, name="contact"),
    path("profile/<int:id>", profilePageView, name="profile")
]