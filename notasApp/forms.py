from django import forms
from .models import NotasModel, CategoriaNotasModel

class NotasForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=CategoriaNotasModel.objects.all(),
        widget=forms.SelectMultiple(attrs={'class':'custom-select'})
        )

    class Meta:
        model = NotasModel
        fields = ['titulo', 'camponota', 'categorias']
        labels = {
            'titulo':'Agrega tu titulo',
            'camponota':'Escribe tu nota aquí',
        }
        widgets = {
            'autor': forms.HiddenInput(),
        }
