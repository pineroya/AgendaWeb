from django import forms
from .models import NotasModel, CategoriaNotasModel

class NotasForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(queryset=CategoriaNotasModel.objects.all())

    class Meta:
        model = NotasModel
        fields = ['titulo', 'camponota', 'categorias']
        widgets = {
            'autor': forms.HiddenInput(),
        }
