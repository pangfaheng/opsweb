import os
from django.shortcuts import render, redirect, get_object_or_404
from example.models import InstanceBaseInfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from example.forms import TaskListForm, TerraformProjectForm
from example.models import TaskList, TerraformProject
from django.urls import reverse
from django.views.decorators.cache import never_cache


def to_root_home(request):
    return redirect(request, "sysadmin/home.html")


def home(request):
    return render(request, "example/home.html")


def __server_assets_total(data):
    return len(data)


def previous(request):
    queryset = InstanceBaseInfo.objects.filter().order_by("id")
    data = InstanceBaseInfo.objects.all()
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


def file_manager(request):
    context = {}
    files = os.listdir(settings.MEDIA_ROOT)
    context["files"] = files
    return render(request, "example/file_manager.html", context)


def file_manager_download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            response = HttpResponse(
                file.read(), content_type="application/octet-stream"
            )
            response[
                "Content-Disposition"
            ] = f"attachment; filename={os.path.basename(file_path)}"
        return response
    else:
        return Http404("File not found.")


def file_manager_upload(request):
    if request.method == "POST" and request.FILES["upload"]:
        upload = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return redirect("file_manager_success", file_url=file_url)
    return render(request, "example/file_manager_upload.html")


def file_manager_success(request, file_url):
    return render(request, "example/file_manager_success.html", {"file_url": file_url})


def task_list(request):
    tasks = TaskList.objects.all()
    return render(
        request,
        "example/task_list.html",
        {
            "tasks": tasks,
        },
    )


def task_create(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("task_list"))
    else:
        form = TaskListForm()
    return render(
        request,
        "example/task_form.html",
        {
            "form": form,
        },
    )


def task_detail(request, pk):
    task = get_object_or_404(TaskList, pk=pk)
    return render(
        request,
        "example/task_detail.html",
        {
            "task": task,
        },
    )


def task_update(request, pk):
    task_obj = get_object_or_404(TaskList, pk=pk)
    if request.method == "POST":
        form = TaskListForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "task_detail",
                    args=[
                        pk,
                    ],
                )
            )
    else:
        form = TaskListForm(instance=task_obj)
    return render(request, "example/task_form.html", {"form": form, "object": task_obj})


def task_delete(request, pk):
    task_obj = get_object_or_404(TaskList, pk=pk)
    task_obj.delete()
    return redirect(reverse("task_list"))


@never_cache
def terraform_home(request):
    return render(request, "example/terraform_home.html")


@never_cache
def terraform_project_list(request):
    queryset = TerraformProject.objects.filter().order_by("id")
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
    }
    return render(request, "example/terraform_project_list.html", context)


@never_cache
def terraform_create_project(request):
    if request.method == "POST":
        form = TerraformProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "terraform_home",
                )
            )
    else:
        form = TerraformProjectForm()
    return render(
        request,
        "example/terraform_create_project.html",
        {
            "form": form,
        },
    )


@never_cache
def terraform_detail_project(request):
    if request.method == "POST":
        form = TerraformProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "terraform_home",
                )
            )
    else:
        form = TerraformProjectForm()
    return render(
        request,
        "example/terraform_create_project.html",
        {
            "form": form,
        },
    )


@never_cache
def terraform_update_project(request, pk):
    project_obj = get_object_or_404(TerraformProject, pk=pk)
    if request.method == "POST":
        form = TerraformProjectForm(instance=project_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "terraform_update_project",
                    args=[
                        pk,
                    ],
                )
            )
    else:
        form = TaskListForm(instance=project_obj)
    return render(
        request,
        "example/terraform_update_project.html",
        {"form": form, "object": project_obj},
    )


@never_cache
def terraform_delete_project(request, pk):
    project_obj = get_object_or_404(TerraformProject, pk=pk)
    if request.method == "POST":
        form = TerraformProjectForm(instance=project_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "terraform_delete_project",
                    args=[
                        pk,
                    ],
                )
            )
    else:
        form = TaskListForm(instance=project_obj)
    return render(
        request,
        "example/terraform_delete_project.html",
        {"form": form, "object": project_obj},
    )


@never_cache
def terraform_select(request):
    pass


@never_cache
def terraform_create_template(request):
    return render(request, "example/terraform_create_template.html")


@never_cache
def terraform_delete(request):
    pass


@never_cache
def terraform_update(request):
    pass


@never_cache
def terraform_new(request):
    pass


@never_cache
def terraform_check(request):
    pass


@never_cache
def terraform_plan(request):
    pass


def terraform_apply(request):
    pass
