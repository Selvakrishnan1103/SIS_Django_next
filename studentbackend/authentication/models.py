from django.db import models

class parent(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    parent_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='parent_photos/', null=True, blank=True)

    def __str__(self):
        return self.parent_name



# Create your models here.
