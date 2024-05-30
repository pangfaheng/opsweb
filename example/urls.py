from django.urls import path
from example import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.example_home, name="example_home"),
    # 示例：分页链接
    path("previous", views.example_previous_001, name="example_previous_001"),
    # 示例：上传、下载文件
    path('file_manager', views.example_file_manager, name='example_file_manager'),
    path('file_manager/create_file', views.example_file_manager_create_file, name='example_file_manager_create_file'),
    path('file_manager/download_file', views.example_file_manager_download_file, name='example_file_manager_download_file'),
    path('file_manager/upload_file', views.example_file_manager_upload_file, name='example_file_manager_upload_file'),
    path('file_manager/upload_success/<path:file_url>/', views.example_file_manager_upload_success, name='example_file_manager_upload_success'),
]
urlpatterns += staticfiles_urlpatterns()


