from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("hello", views.home, name="herro_home"),
    path("hello/<name>", views.hello_there, name="hello_home_there"),
    path("hello/about/", views.about, name="herro_about"),
    path("hello/contact/", views.contact, name="herro_contact"),
    path("hello/log/", views.log_message, name="herro_log"),
]
urlpatterns += staticfiles_urlpatterns()
