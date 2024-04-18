from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
]


urlpatterns += staticfiles_urlpatterns()
