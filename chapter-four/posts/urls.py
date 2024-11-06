from django.urls import path
from .views import homeView, PostPageView

urlpatterns = [
    path("", homeView, name="home"),
    path("posts", PostPageView.as_view(), name="posts")
]