from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id, self.department_name
    
class Section(models.Model):
    section_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_name + ' , ' + self.department.department_name
    
class User(AbstractUser):
    section_id = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
class Documents(models.Model):
    doc_title = models.CharField(max_length=100)
    doc_number = models.CharField(max_length=100)
    doc_date = models.DateField(auto_now_add=True)
    document_submission_date = models.DateTimeField(auto_now_add=True)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    doc_details = models.TextField(max_length=300)
    

    def __str__(self):
        return self.doc_title + ' ' + self.doc_number + ',' + ' ' + self.employee_id.username
class Document_Procedures(models.Model):
    document = models.ForeignKey(Documents, related_name='documents', on_delete=models.CASCADE)
    doc_destination = models.ForeignKey(User, related_name='reciver', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.document.doc_title + ',' + 'sent to: ' +  self.doc_destination.username

class Logs(models.Model):
    document_log_id = models.ForeignKey(Documents, related_name='docuemnent_log', on_delete=models.CASCADE)
    details = models.TextField(max_length=300)