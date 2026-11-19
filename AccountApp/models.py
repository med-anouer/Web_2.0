from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True)
    Phone_number = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField("AccountApp.Specialty", related_name='doctors')
        
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)   
    phone_number = models.CharField(max_length=8)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        

    # Add any additional fields specific to doctors