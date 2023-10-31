from django import forms
from django.utils import timezone

class ContactoForm(forms.Form):
    email = forms.EmailField(label='Tu mail de contacto', required=True)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['fecha'] = timezone.now()
        return cleaned_data
