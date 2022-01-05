from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name', 'description', 'image']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date']
