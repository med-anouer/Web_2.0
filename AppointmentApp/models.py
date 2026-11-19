from django.db import models

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(blank=True, upload_to='prescriptions/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        


class Status(models.TextField):
    PENDING = "Pending" , "en attente"
    CONFIRMED = "Confirmed" , "confirmé"
    CANCELED = "Canceled" , "annulé"
    Status = models.CharField(max_length=20, choices=Status.choices, default=PENDING)
    duration_minutes = models.PositiveIntegerField()
    appointement_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    
