from django.db import models

class student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student_image = models.ImageField(upload_to='student_images/',)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_no = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    CLASS_CHOICES = [
        ('LKG', 'LKG'),
        ('UKG', 'UKG'),
        ('1', '|'),
        ('2', '||'),
        ('3', '|||'),
    ]
    section = models.CharField(max_length=1)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    Religion = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    Mother_tongue = models.CharField(max_length=20)
    Gender_CHOICES = [
        ('M','Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=10, choices=Gender_CHOICES)
    email = models.EmailField()
    address = models.TextField()
    



# Create your models here.
