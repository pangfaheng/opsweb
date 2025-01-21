from django.urls import path, re_path
from example import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="example_home"),
    path("../", views.to_root_home, name="to_root_home"),
    path("previous", views.previous, name="previous"),
    path("file_manager", views.file_manager, name="file_manager"),
    path(
        "file_manager/download/<str:filename>",
        views.file_manager_download,
        name="file_manager_download",
    ),
    path(
        "file_manager/upload",
        views.file_manager_upload,
        name="file_manager_upload",
    ),
    path(
        "file_manager/success/<path:file_url>/",
        views.file_manager_success,
        name="file_manager_success",
    ),
    path("task", views.task_list, name="task_list"),
    path("task/create", views.task_create, name="task_create"),
    re_path(r"^(?P<pk>\d+)/$", views.task_detail, name="task_detail"),
    re_path(r"^(?P<pk>\d+)/update/$", views.task_update, name="task_update"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.task_delete, name="task_delete"),
    path(
        "terraform/home",
        views.terraform_home,
        name="terraform_home",
    ),
    path(
        "terraform/project",
        views.terraform_project_list,
        name="terraform_project_list",
    ),
    path(
        "terraform/create_project",
        views.terraform_create_project,
        name="terraform_create_project",
    ),
    re_path(
        r"^(?P<project_id>\d+)/$",
        views.terraform_detail_project,
        name="terraform_detail_project",
    ),
    re_path(
        r"^(?P<project_id>\d+)/update/$",
        views.terraform_update_project,
        name="terraform_update_project",
    ),
    re_path(
        r"^(?P<project_id>\d+)/delete/$",
        views.terraform_delete_project,
        name="terraform_delete_project",
    ),
    path(
        "terraform/create_template",
        views.terraform_create_template,
        name="terraform_create_template",
    ),
]
urlpatterns += staticfiles_urlpatterns()
