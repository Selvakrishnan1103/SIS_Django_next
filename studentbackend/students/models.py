from django.db import models
from django.core.validators import MinLengthValidator

class student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student_image = models.ImageField(upload_to='student_images/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    admission_no = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(unique=True)
    phone = models.ImageField(max_length=10,validators=[MinLengthValidator(10)],unique=True,null=True)
    dob = models.DateField()
    admission_date = models.DateTimeField(null=True,auto_now_add=True)
    vechile_type = models.CharField(max_length=20,null=True)
    route_name = models.CharField(max_length=20,null=True)
    vechile_no = models.CharField(max_length=20,null=True)
    dayscholer_or_hosteller = models.CharField(choices=[('Dayscholer', 'Dayscholer'), ('Hostel', 'Hosteller')], max_length=20,default='Dayscholer')
    room_no = models.CharField(max_length=10, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True,validators=[MinLengthValidator(11)], blank=True)
    ifsc_code = models.CharField(max_length=11, null=True, blank=True,unique=True)
    account_no = models.IntegerField(unique=True,null=True, blank=True)
    branch = models.CharField(max_length=20, null=True, blank=True)
    academic_year = models.CharField(max_length=20, null=True, blank=True)

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
    Mother_tongue = models.CharField(max_length=20)
    Gender_CHOICES = [
        ('M','Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=10, choices=Gender_CHOICES)
    address = models.TextField()
    



# Create your models here.
