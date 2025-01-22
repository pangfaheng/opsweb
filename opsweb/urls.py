from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),  # UI Kits Html files
]
