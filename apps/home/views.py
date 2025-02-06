from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Category


@login_required
def home(request):
    categories = Category.objects.all()
    return render(request, "home/index.html", {"categories": categories})
