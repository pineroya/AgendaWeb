from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CategoriaNotasModel(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class NotasModel(models.Model):
    titulo = models.CharField(max_length=50)
    camponota = models.TextField(max_length=600)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categorias = models.ManyToManyField(CategoriaNotasModel)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        return self.titulo
    
