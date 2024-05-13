from django.shortcuts import render
from sysadmin.models import instance_base_info

def sysadmin_home(request):
    return render(request, "sysadmin/home.html")

def sysadmin_server_assets(request):
    data = instance_base_info.objects.all()
    return render(request, "sysadmin/sysadmin_server_assets.html", {'data': data,})