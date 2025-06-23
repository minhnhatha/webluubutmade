from django.contrib import admin
from home.models import *
# Register your models here.
admin.site.register(File)
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    readonly_fields = ['date', 'update']