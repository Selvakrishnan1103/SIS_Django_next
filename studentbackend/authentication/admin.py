from django.contrib import admin
from .models import parent

@admin.register(parent)
class ParentAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = [ 'parent_name', 'profile_photo', 'parent_photo', 'created_at', 'email', 'contact_number', 'parent_Occupation']
=======
    list_display = [ 'parent_name', 'profile_photo', 'photo', 'created_at']
>>>>>>> 17a22eb3c272280defd2407206770bc2ccb08923
