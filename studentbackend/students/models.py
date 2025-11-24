from django.db import models

class student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=1)


# Create your models here.
