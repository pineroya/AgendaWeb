import email
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    website_url=models.CharField(max_length=255, default='')
