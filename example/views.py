from django.shortcuts import render
from example.models import instance_base_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def example_home(request):
    return render(request, "example/home.html")

def __server_assets_total(data):
    return len(data)

def example_previous_001(request):
    queryset = instance_base_info.objects.filter().order_by('id')
    data = instance_base_info.objects.all()
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {'page_obj': page_obj, 'is_paginated': is_paginated, 'data': data, 'server_total': __server_assets_total(data = data)}
    print(context)
    return render(request, 'example/previous_001.html', context)
