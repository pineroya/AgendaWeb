from django import forms
from django.utils import timezone


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    asunto = forms.CharField(max_length=200, label='Asunto', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(label = 'Mensaje', widget=forms.Textarea(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['fecha'] = timezone.now()
        return cleaned_data