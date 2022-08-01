from django.contrib import admin

# Register your models here.

from main.models import CategoryModel, InstitutionModel




@admin.register(CategoryModel)
class CategoryModel(admin.ModelAdmin):
    pass




@admin.register(InstitutionModel)
class InstitutionModel(admin.ModelAdmin):
    pass
