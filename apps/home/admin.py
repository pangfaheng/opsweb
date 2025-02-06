from django.contrib import admin

from .models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1  # 默认添加一条空白记录


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]  # 在 Category 页面下显示 SubCategory


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
