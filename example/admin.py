from django.contrib import admin

from .models import (
    InstanceBaseInfo,
    TaskList,
    TerraformEnvironmentTemplate,
    TerraformEnvironments,
    TerraformCodeTemplate,
)

# Register your models here.
admin.site.register(InstanceBaseInfo)
admin.site.register(TaskList)
admin.site.register(TerraformEnvironmentTemplate)
admin.site.register(TerraformEnvironments)
admin.site.register(TerraformCodeTemplate)
