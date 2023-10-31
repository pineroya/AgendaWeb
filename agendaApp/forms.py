from django import forms
from .models import AgendaModel

class agendaForm(forms.ModelForm):
    tel_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'contact_field'}))
    email = forms.EmailField(widget=forms.TextInput())

    class Meta:
        model = AgendaModel
        fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']
