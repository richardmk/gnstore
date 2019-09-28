from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name','state','created']
    resource_class = CategoryResources

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
admin.site.register(Sex)
