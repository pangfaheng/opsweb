import os
from django.shortcuts import render
from example.models import instance_base_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def example_home(request):
    return render(request, "example/home.html")

def __server_assets_total(data):
    return len(data)

def example_previous_001(request):
    queryset = instance_base_info.objects.filter().order_by('id')
    data = instance_base_info.objects.all()
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {'page_obj': page_obj, 'is_paginated': is_paginated, 'data': data, 'server_total': __server_assets_total(data = data)}
    return render(request, 'example/previous_001.html', context)

def example_file_manager(request):
    return render(request, 'example/file_manager.html')

def example_file_manager_create_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'test.txt')
    with open(file_path, 'w') as f:
        f.write('123')
    return render(request, 'example/file_manager.html')

def example_file_manager_download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'test.txt')
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="test.txt"'
        return response
    else:
        return HttpResponse("File not found.")

def example_file_manager_upload_file(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return redirect('example_file_manager_upload_success', file_url=file_url)
    return render(request, 'example/file_manager_upload_file.html')

def example_file_manager_upload_success(request, file_url):
    return render(request, 'example/file_manager_upload_success.html', {'file_url': file_url})
