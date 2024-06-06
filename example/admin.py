from django.contrib import admin

from .models import InstanceBaseInfo, TaskList

# Register your models here.
admin.site.register(InstanceBaseInfo)
admin.site.register(TaskList)
