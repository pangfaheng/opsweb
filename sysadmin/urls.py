from django.urls import path
from sysadmin import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.sysadmin_home, name="sysadmin_home"),
    path("server/", views.sysadmin_server_assets, name="sysadmin_server_assets"),
    path("server2/", views.sysadmin_server_assets_2, name="sysadmin_server_assets_2"),
]
urlpatterns += staticfiles_urlpatterns()
