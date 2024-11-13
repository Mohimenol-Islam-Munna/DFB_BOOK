from django.urls import path
from .views import homeView, PostPageView

urlpatterns = [
    path("posts/", PostPageView.as_view(),name="posts"),
    path("", homeView, name="home"),
]