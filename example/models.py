from django.db import models


class InstanceBaseInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_id = models.CharField(
        verbose_name="Instance ID", max_length=100, unique=True
    )
    instance_name = models.CharField(max_length=100)
    instance_cpu_size = models.IntegerField()
    instance_memory_size = models.IntegerField()
    instance_system_disk_type = models.CharField(max_length=100)
    instance_system_disk_size = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.instance_id


class TaskStatus(models.TextChoices):
    UNSTARTED = "u", "Not Started"
    EXECUTING = "e", "Executing"
    FINISHED = "f", "Finished"


class TaskList(models.Model):
    name = models.CharField(verbose_name="Task Name", max_length=120, unique=True)
    status = models.CharField(
        verbose_name="Task Status", max_length=1, choices=TaskStatus.choices
    )
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_type = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
    )
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name


class TerraformEnvironmentTemplate(models.Model):
    environment_context = models.TextField()
    file_name = models.CharField(max_length=100)
    template_id = models.CharField(max_length=100)

    def __str__(self):
        return self.template_id


class TerraformEnvironments(models.Model):
    cloud = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    backend_object_type = models.CharField(max_length=100)
    backend_object_name = models.CharField(max_length=100)
    template_id = models.CharField(max_length=100)
    env_id = models.CharField(max_length=100)

    def __str__(self):
        return self.env_id


class TerraformCodeTemplate(models.Model):
    module = models.CharField(max_length=100)
    block_type = models.CharField(max_length=100)
    block_label = models.CharField(max_length=100)
    block_label_name = models.CharField(max_length=100)
    block_context = models.TextField()
    file_name = models.CharField(max_length=100)
    env_id = models.CharField(max_length=100)
    code_id = models.CharField(max_length=100)

    def __str__(self):
        return self.block_label
