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
    id = models.BigAutoField(primary_key=True)
    environment_context = models.TextField()
    file_name = models.CharField(max_length=100)
    remark = models.CharField(max_length=300)
    env_template_id = models.CharField(max_length=100)

    def __str__(self):
        text = self.file_name + " - " + self.remark
        return text


class TerraformEnvironment(models.Model):
    id = models.BigAutoField(primary_key=True)
    cloud = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    backend_type = models.CharField(max_length=100)
    backend_bucket = models.CharField(max_length=100)
    backend_region = models.CharField(max_length=100)
    env_template_id = models.CharField(max_length=100)
    env_id = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        text = "项目: " + self.project + ", 云服务: " + self.cloud + ", 地域: " + self.region
        return text


class TerraformCodeTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    block_type = models.CharField(max_length=100)
    block_label = models.CharField(max_length=100)
    block_label_name = models.CharField(max_length=100)
    block_context = models.TextField()
    code_template_id = models.CharField(max_length=100)

    def __str__(self):
        return self.block_label


class TerraformCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.JSONField()
    status = models.BooleanField()
    env_id = models.CharField(max_length=100)
    code_template_id = models.CharField(max_length=100)
    code_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.data)


class TerraformCodeAtModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    src_module = models.CharField(max_length=100)
    src_output = models.CharField(max_length=100)
    dest_module = models.CharField(max_length=100)
    dest_input = models.CharField(max_length=100)
    status = models.BooleanField()
    code_template_id = models.CharField(max_length=100)
    at_module_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dest_input)


class TerraformOutputCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    output_type = models.CharField(max_length=100)
    status = models.BooleanField()
    code_id = models.CharField(max_length=100)
    at_module_id = models.CharField(max_length=100)
    output_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
