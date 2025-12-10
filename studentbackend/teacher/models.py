from django.db import models

class teacher(models.Model):
    teacher_image = models.ImageField(upload_to='teacher_image/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20,null=True)
    Role = models.CharField( choices=[('teacher','teacher'),('Accountant','Accountant'),('Librarian','Librarian')],null=True,max_length=209)
    Gender = models.CharField(max_length=10,null=True)
    phone = models.IntegerField(null=True)
    Blood_group = models.CharField(max_length=10,null=True)
    Marital_Status = models.CharField(max_length=20,null=True)
    Father_name = models.CharField(max_length=20,null=True)
    Mother_name = models.CharField(max_length=20,null=True)
    dob = models.DateField(null=True)
    Date_of_joining = models.DateField(null=True)
    Language_Known = models.CharField(max_length=100,null=True)
    Qualification = models.CharField(max_length=50,null=True)
    Work_Experience = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    Epf_no = models.IntegerField(null=True)
    Basic_salary = models.IntegerField(null=True)
    Contract_type = models.CharField(max_length=20,null=True)
    Account_name = models.CharField(max_length=20,null=True)
    Account_Number = models.IntegerField(null=True)
    Bank_name = models.CharField(max_length=20,null=True)
    IFSC_code = models.CharField(max_length=11,null=True)
    Branch_name = models.CharField(max_length=10,null=True)
    Use_School_bus = models.CharField(choices=[('Yes','Yes'),('NO','No')],null=True,max_length=10)
    Route = models.CharField(max_length=10,null=True)
    Vechicle_Number = models.CharField(max_length=20,null=True)
    Pickup_point = models.CharField(max_length=20,null=True)
    Resume = models.FileField(upload_to='Resume/',null=True)
    Joining_Letter = models.FileField(upload_to='Letter/',null=True)
    


# Create your models here.
