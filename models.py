# models.py
from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Signup(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField()

class Input(models.Model):
    desc = models.TextField()

class Input1(models.Model):
    data = models.TextField()

class AudioUpload(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class Application(models.Model):
    ACCEPTED = 'Accept'
    REJECTED = 'Reject'
    
    STATUS_CHOICES = [
        (ACCEPTED, 'Accept'),
        (REJECTED, 'Reject'),
    ]
    
    applicant_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACCEPTED)

    def __str__(self):
        return f'{self.applicant_name} - {self.status}'


class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
