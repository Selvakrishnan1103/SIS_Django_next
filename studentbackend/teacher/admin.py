from django.contrib import admin
from .models import teacher

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['class_teacher_name', 'mark_sheet', 'created_at']


# Register your models here.
