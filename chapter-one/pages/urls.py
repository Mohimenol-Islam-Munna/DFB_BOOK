from django.urls import path
<<<<<<< HEAD
from .views import homePageView, AboutPageView

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/", AboutPageView.as_view(), name="about/"),
=======
from .views import homePageView, aboutPageView, contactPageView, profilePageView


urlpatterns = [
    path("", homePageView, name="home"),
    path("about", aboutPageView, name="about"),
    path("contact", contactPageView, name="contact"),
    path("profile/<int:id>", profilePageView, name="profile")
>>>>>>> 74c72c099d8869338ebbe664d640e1da213497f1
]