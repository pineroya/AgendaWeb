from django import forms
from .models import ContactoModel

class ContactoForm(forms.ModelForm):
    class Meta:
        model = ContactoModel
        fields = ('nombre', 'correo', 'asunto', 'mensaje')