from django.shortcuts import render

def sysadmin_home(request):
    return render(request, "sysadmin/home.html")
