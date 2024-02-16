from django.db import models

# Create your models here.
class JobDetails(models.Model):
    role=models.CharField(max_length=1500,blank=True,null=True)
    company_name=models.CharField(max_length=1500,blank=True,null=True)
    experience=models.CharField(max_length=1500,blank=True,null=True)
    ctc=models.CharField(max_length=1500,blank=True,null=True)
    link=models.CharField(max_length=1500,blank=True,null=True)
    location=models.CharField(max_length=1500,blank=True,null=True)
    def __str__(self):
        return self.company_name
class PlacementDetails(models.Model):
    name=models.CharField(max_length=30)
    company_name=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    ctc=models.CharField(max_length=50)
    batch=models.CharField(max_length=50)
    
