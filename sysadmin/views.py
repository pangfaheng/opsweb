from django.shortcuts import render

def sysadmin_home(request):
    return render(request, "sysadmin/home.html")

def sysadmin_server_assets(request):
    return render(request, "sysadmin/sysadmin_server_assets.html")