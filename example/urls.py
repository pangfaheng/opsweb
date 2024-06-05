from django.urls import path, re_path
from example import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.example_home, name="example_home"),
    # 示例：分页链接
    path("previous", views.example_previous, name="example_previous"),
    # 示例：上传、下载文件
    path("file_manager", views.example_file_manager, name="example_file_manager"),
    path(
        "file_manager/create_file",
        views.example_file_manager_create_file,
        name="example_file_manager_create_file",
    ),
    path(
        "file_manager/download_file",
        views.example_file_manager_download_file,
        name="example_file_manager_download_file",
    ),
    path(
        "file_manager/upload_file",
        views.example_file_manager_upload_file,
        name="example_file_manager_upload_file",
    ),
    path(
        "file_manager/upload_success/<path:file_url>/",
        views.example_file_manager_upload_success,
        name="example_file_manager_upload_success",
    ),
    path("task/create", views.task_create, name="task_create"),
    path("task", views.task_list, name="task_list"),
    re_path(r"^(?P<pk>\d+)/$", views.task_detail, name="task_detail"),
    re_path(r"^(?P<pk>\d+)/update/$", views.task_update, name="task_update"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.task_delete, name="task_delete"),
]
urlpatterns += staticfiles_urlpatterns()
