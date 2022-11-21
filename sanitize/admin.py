from django.contrib import admin
from .models import FbFile


@admin.register(FbFile)
class FbFileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'date_added']
