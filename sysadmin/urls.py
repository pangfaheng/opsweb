from django.urls import path
from sysadmin import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.sysadmin_home, name="sysadmin_home"),
]
urlpatterns += staticfiles_urlpatterns()
