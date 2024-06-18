from django.contrib import admin

from .models import (
    TerraformEnvironmentTemplate,
    TerraformEnvironment,
    TerraformCodeTemplate,
    TerraformCode,
    TerraformOutputAtModule,
    TerraformOutputCode,
    TerraformProject,
)

# Register your models here.
admin.site.register(TerraformEnvironmentTemplate)
admin.site.register(TerraformEnvironment)
admin.site.register(TerraformCodeTemplate)
admin.site.register(TerraformCode)
admin.site.register(TerraformOutputAtModule)
admin.site.register(TerraformOutputCode)
admin.site.register(TerraformProject)
