from django.db import models

class sysadmin_instance_base_info(models.Model):
    id                        = models.BigAutoField(primary_key=True)
    instance_id               = models.CharField(max_length=100, unique=True)
    instance_name             = models.CharField(max_length=100)
    instance_cpu_size         = models.IntegerField()
    instance_memory_size      = models.IntegerField()
    instance_system_disk_type = models.CharField(max_length=100)
    instance_system_disk_size = models.IntegerField()
    create_time               = models.DateTimeField(auto_now_add=True)
    update_time               = models.DateTimeField(auto_now=True)


class sysadmin_instance_tags_info(models.Model):
    ENVIRONMENT = "Environment"
    PROJECT     = "Project"
    SERVICE     = "Service"
    COMPANY     = "Company"
    TEAM        = "Team"
    OWNER       = "Owner"
    ROLE        = "Role"
    CLOUD       = "Cloud"
    REGION      = "Region"
    AREA        = "Area"
    BILL        = "Bill"
    TAG_KEY_CHOICES = {
        ENVIRONMENT : "环境",
        PROJECT     : "项目",
        SERVICE     : "服务",
        COMPANY     : "公司",
        TEAM        : "团队",
        OWNER       : "负责人",
        ROLE        : "权限",
        CLOUD       : "云服务商",
        REGION      : "地理意义上的区域",
        AREA        : "虚拟意义上的区域",
        BILL        : "财务负责人",
    }
    id          = models.BigAutoField(primary_key=True)
    instance_id = models.CharField(max_length=100)
    tag_key     = models.CharField(max_length=300, choices=TAG_KEY_CHOICES)
    tag_value   = models.CharField(max_length=300)
    tag_status  = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=["instance_id", "tag_key"]),
        ]


class sysadmin_instance_data_disk_info(models.Model):
    id                        = models.BigAutoField(primary_key=True)
    instance_id               = models.CharField(max_length=100)
    instance_data_disk_dir    = models.CharField(max_length=300)
    instance_data_disk_device = models.CharField(max_length=300)
    instance_data_disk_type   = models.CharField(max_length=100)
    instance_data_disk_size   = models.IntegerField()
    create_time               = models.DateTimeField(auto_now_add=True)
    update_time               = models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=["instance_id"]),
        ]


class sysadmin_instance_connect_info(models.Model):
    id          = models.BigAutoField(primary_key=True)
    instance_id = models.CharField(max_length=100)
    address     = models.CharField(max_length=100)
    domain      = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=["instance_id"]),
        ]