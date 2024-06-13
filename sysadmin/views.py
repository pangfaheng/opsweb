from django.shortcuts import render, redirect
from sysadmin.models import instance_base_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def sysadmin_home(request):
    return render(request, "sysadmin/home.html")


def to_example(request):
    # 跳转到 example 的 index 页面
    return redirect("example_home")


def __sysadmin_server_assets_total(data):
    return len(data)


def sysadmin_server_assets(request):
    data = instance_base_info.objects.all()
    return render(
        request,
        "sysadmin/sysadmin_server_assets.html",
        {"data": data, "server_total": __sysadmin_server_assets_total(data=data)},
    )


def example_previous_001(request):
    queryset = instance_base_info.objects.filter().order_by("id")
    data = instance_base_info.objects.all()
    paginator = Paginator(queryset, 5)
    page = request.GET.get("page")
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {
        "page_obj": page_obj,
        "is_paginated": is_paginated,
        "data": data,
        "server_total": __sysadmin_server_assets_total(data=data),
    }
    print(context)
    return render(request, "sysadmin/example_previous_001.html", context)
