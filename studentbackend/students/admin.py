from django.contrib import admin
from .models import student

@admin.register(student)
 
class StudentAdmin(admin.ModelAdmin):
     list_display = ['id', 'first_name', 'last_name', 'age', 'email', 'phone', 'dob', 'class_name', 'section', 'blood_group', 'gender', 'address',
                     'vechile_type','route_name','vechile_no','dayscholer_or_hosteller','room_no','bank_name','ifsc_code',
                     'account_no','branch','academic_year','admission_date']

     list_filter = ['class_name', 'section', 'age']