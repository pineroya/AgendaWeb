from django.db import models

# Create your models here.

class AgendaModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel_number = models.IntegerField()
    addres = models.CharField(max_length=140)
    email = models.EmailField()
    web = models.CharField(max_length=240)
    bio = models.TextField(max_length=300)
    picture = models.ImageField(upload_to='agenda')
