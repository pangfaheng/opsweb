from django.urls import path, re_path
from example import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("previous", views.previous, name="previous"),
    path("file_manager", views.file_manager, name="file_manager"),
    path(
        "file_manager/create_file",
        views.file_manager_create_file,
        name="file_manager_create_file",
    ),
    path(
        "file_manager/download_file",
        views.file_manager_download_file,
        name="file_manager_download_file",
    ),
    path(
        "file_manager/upload_file",
        views.file_manager_upload_file,
        name="file_manager_upload_file",
    ),
    path(
        "file_manager/upload_success/<path:file_url>/",
        views.file_manager_upload_success,
        name="file_manager_upload_success",
    ),
    path("task", views.task_list, name="task_list"),
    path("task/create", views.task_create, name="task_create"),
    re_path(r"^(?P<pk>\d+)/$", views.task_detail, name="task_detail"),
    re_path(r"^(?P<pk>\d+)/update/$", views.task_update, name="task_update"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.task_delete, name="task_delete"),
]
urlpatterns += staticfiles_urlpatterns()
