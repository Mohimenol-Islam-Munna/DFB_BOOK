from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("custom_auth.urls")),
    path("blog/", include("blog.urls")),
    path("", include("posts.urls")),
]
