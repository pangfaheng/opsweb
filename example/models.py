from django.db import models


class InstanceBaseInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_id = models.CharField(max_length=100, unique=True)
    instance_name = models.CharField(max_length=100)
    instance_cpu_size = models.IntegerField()
    instance_memory_size = models.IntegerField()
    instance_system_disk_type = models.CharField(max_length=100)
    instance_system_disk_size = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class TaskStatus(models.TextChoices):
    UNSTARTED = "u", "Not Started"
    EXECUTING = "e", "Executing"
    FINISHED = "f", "Finished"


class TaskList(models.Model):
    name = models.CharField(verbose_name="Task Name", max_length=120, unique=True)
    status = models.CharField(
        verbose_name="Task Status", max_length=1, choices=TaskStatus.choices
    )

    def __str__(self):
        return self.name
