from django.contrib import admin

from .models import teacher

@admin.register(teacher)

class Teacheradmin(admin.ModelAdmin):
    list_display = ["first_name"]
