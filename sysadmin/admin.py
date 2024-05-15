from django.contrib import admin

from .models import instance_cloud_info
from .models import instance_base_info
from .models import instance_tags_info
from .models import instance_data_disk_info
from .models import instance_connect_info

# Register your models here.
admin.site.register(instance_cloud_info)
admin.site.register(instance_base_info)
admin.site.register(instance_tags_info)
admin.site.register(instance_data_disk_info)
admin.site.register(instance_connect_info)

