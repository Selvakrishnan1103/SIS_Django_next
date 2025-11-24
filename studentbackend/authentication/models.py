from django.db import models

class parent(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    parent_name = models.CharField(max_length=100)
    parent_photo = models.ImageField(upload_to='parents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



# Create your models here.
