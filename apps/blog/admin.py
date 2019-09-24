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

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name','email','state','created']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title','author','categories','state','created']

    def categories(self,obj):
        return ", ".join([c.name for c in obj.category.all().order_by("name")])

admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)