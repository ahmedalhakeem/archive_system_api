from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department_name
    
class Section(models.Model):
    section_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_name + ' , ' + self.department.department_name
    
class User(AbstractUser):
    pass
    
class Documents(models.Model):
    title = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    document_date = models.DateField(auto_now_add=True)
    document_time_delivey = models.DateTimeField(auto_now_add=True)
    issuer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    to_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.document_number
    