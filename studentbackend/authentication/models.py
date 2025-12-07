from django.db import models

class parent(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_Occupation = models.CharField(max_length=100,)
    parent_address = models.TextField(null=True)


# Create your models here.
