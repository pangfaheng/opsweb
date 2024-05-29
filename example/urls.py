from django.urls import path
from example import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.example_home, name="example_home"),
    # 示例：分页链接
    path("previous", views.example_previous_001, name="example_previous_001"),
]
urlpatterns += staticfiles_urlpatterns()
