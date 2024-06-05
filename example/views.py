import os
from django.shortcuts import render, redirect, get_object_or_404
from example.models import instance_base_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.http import Http404
from example.forms import single_task_form
from example.models import single_task_task
from django.urls import reverse


def example_home(request):
    return render(request, "example/home.html")


def __server_assets_total(data):
    return len(data)


def example_previous(request):
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
        "server_total": __server_assets_total(data=data),
    }
    return render(request, "example/previous.html", context)


def example_file_manager(request):
    return render(request, "example/file_manager.html")


def example_file_manager_create_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "test.txt")
    with open(file_path, "w") as f:
        f.write("123")
    return render(request, "example/file_manager.html")


def example_file_manager_download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "test.txt")
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, "rb"))
        response["Content-Disposition"] = 'attachment; filename="test.txt"'
        return response
    else:
        return Http404("File not found.")
        return HttpResponse("File not found.")


def example_file_manager_upload_file(request):
    if request.method == "POST" and request.FILES["upload"]:
        upload = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return redirect("example_file_manager_upload_success", file_url=file_url)
    return render(request, "example/file_manager_upload_file.html")


def example_file_manager_upload_success(request, file_url):
    return render(
        request, "example/file_manager_upload_success.html", {"file_url": file_url}
    )


# Create a task
def task_create(request):
    # 如果用户通过POST提交，通过request.POST获取提交数据
    if request.method == "POST":
        # 将用户提交数据与TaskForm表单绑定
        form = TaskForm(request.POST)
        # 表单验证，如果表单有效，将数据存入数据库
        if form.is_valid():
            form.save()
            # 跳转到任务清单
            return redirect(reverse("tasks:task_list"))
    else:
        # 否则空表单
        form = TaskForm()
    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
        },
    )


# Retrieve task list
def task_list(request):
    # 从数据库获取任务清单
    tasks = Task.objects.all()
    # 指定渲染模板并传递数据
    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
        },
    )


# Retrieve a single task
def task_detail(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task = get_object_or_404(Task, pk=pk)
    return render(
        request,
        "tasks/task_detail.html",
        {
            "task": task,
        },
    )


# Update a single task
def task_update(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象实例
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "tasks:task_detail",
                    args=[
                        pk,
                    ],
                )
            )
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "tasks/task_form.html", {"form": form, "object": task_obj})


# Delete a single task
def task_delete(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()  # 删除然后跳转
    return redirect(reverse("tasks:task_list"))
