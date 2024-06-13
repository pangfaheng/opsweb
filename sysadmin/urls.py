from django.urls import path
from sysadmin import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.sysadmin_home, name="sysadmin_home"),
    path("server/", views.sysadmin_server_assets, name="sysadmin_server_assets"),
    # 示例：分页链接
    path("example/previous", views.example_previous_001, name="example_previous_001"),
    # 前往example
    path("example/", views.to_example, name="to_example"),
]
urlpatterns += staticfiles_urlpatterns()
