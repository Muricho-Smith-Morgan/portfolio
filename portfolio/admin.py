from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'technology', 'image']