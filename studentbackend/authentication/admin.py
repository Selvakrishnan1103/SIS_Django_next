from django.contrib import admin
from .models import parent

@admin.register(parent)
class ParentAdmin(admin.ModelAdmin):

    list_display = [ 'parent_name', 'profile_photo', 'photo', 'created_at']
