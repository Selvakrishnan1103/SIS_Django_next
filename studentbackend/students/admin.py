from django.contrib import admin
from .models import student

@admin.register(student)
 
class StudentAdmin(admin.ModelAdmin):
     list_display = ['id', 'first_name', 'last_name', 'age', 'email', 'phone', 'dob', 'class_name', 'section']

     list_filter = ['class_name', 'section', 'age']
     ordering = ['id']
