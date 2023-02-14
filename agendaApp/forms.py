from django import forms
from .models import AgendaModel
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


class agendaForm(forms.ModelForm):
    model = AgendaModel
    fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']
