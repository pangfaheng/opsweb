from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# 登录视图
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # 登录成功后跳转到主页
    else:
        form = AuthenticationForm()

    return render(request, "authentication/login.html", {"form": form})


# 登出视图
def logout_view(request):
    logout(request)  # 退出登录
    return redirect("home")  # 退出后重定向到主页
