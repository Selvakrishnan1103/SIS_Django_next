from django.db import models

class parent(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    parent_name = models.CharField(max_length=100)
<<<<<<< HEAD
    parent_photo = models.ImageField(upload_to='parents/', null=True, blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_Occupation = models.CharField(max_length=100,)
=======
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='parent_photos/', null=True, blank=True)

    def __str__(self):
        return self.parent_name
>>>>>>> 17a22eb3c272280defd2407206770bc2ccb08923



# Create your models here.
