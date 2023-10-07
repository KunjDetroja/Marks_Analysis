from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MarksResource(resources.ModelResource):
    class Meta:
        model = Marksheet

class MarksAdmin(ImportExportModelAdmin):
    resources_class = MarksResource
    




# Register your models here.
admin.site.register(Marksheet,MarksAdmin)