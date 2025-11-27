from django.db import models

class teacher(models.Model):
    class_teacher_name = models.CharField(max_length=100)
    mark_sheet = models.FileField(upload_to='marksheets/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
