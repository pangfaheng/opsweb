from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", include("hello.urls")),
    path("example/", include("example.urls")),
    path("", include("sysadmin.urls")),
]
