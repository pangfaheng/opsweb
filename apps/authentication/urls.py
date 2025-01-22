from django.urls import path
from apps.authentication import views

urlpatterns = [
    path("login/", views.login_view, name="login"),  # 登录页面
    path("logout/", views.logout_view, name="logout"),  # 退出登录页面
]
