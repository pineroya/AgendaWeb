from django.db import models
from django.contrib.auth.models import User

# Opciones para el campo 'estado'
ESTADO_CHOICES = (
    ('D', 'Borrador'),
    ('P', 'Publicado'),
)

class CalendarioModel(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    texto = models.TextField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.titulo