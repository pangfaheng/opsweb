from django.db import models

class instance_base_info(models.Model):
    id                        = models.BigAutoField(primary_key=True)
    instance_id               = models.CharField(max_length=100, unique=True)
    instance_name             = models.CharField(max_length=100)
    instance_cpu_size         = models.IntegerField()
    instance_memory_size      = models.IntegerField()
    instance_system_disk_type = models.CharField(max_length=100)
    instance_system_disk_size = models.IntegerField()
    create_time               = models.DateTimeField(auto_now_add=True)
    update_time               = models.DateTimeField(auto_now=True)
