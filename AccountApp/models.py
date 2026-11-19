from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    Phone_number = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField("AccountApp.Specialty", related_name='doctors')

number_validator = RegexValidator(regex=r'^\d{8}$', message="Number must be exactly 8 digits.")        
def validate_birth_date(value):
    if value > timezone.now().date():
        raise ValidationError("Birth date cannot be in the future.")

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True , validators=[number_validator])  
    phone_number = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        

    # Add any additional fields specific to doctors