from django.contrib import admin

from .models import (
    TerraformEnvironmentTemplate,
    TerraformEnvironment,
    TerraformCodeTemplate,
    TerraformCode,
    TerraformCodeAtModule,
)

# Register your models here.
admin.site.register(TerraformEnvironmentTemplate)
admin.site.register(TerraformEnvironment)
admin.site.register(TerraformCodeTemplate)
admin.site.register(TerraformCode)
admin.site.register(TerraformCodeAtModule)
