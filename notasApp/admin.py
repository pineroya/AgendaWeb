from django.contrib import admin
from .models import NotasModel, CategoriaNotasModel

# Register your models here.

admin.site.register(NotasModel)
admin.site.register(CategoriaNotasModel)