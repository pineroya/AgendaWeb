from django import forms
from PIL import Image
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.files.uploadedfile import SimpleUploadedFile


class agendaForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    tel_number = forms.IntegerField()
    addres = forms.CharField(max_length=140)
    email = forms.EmailField()
    web = forms.CharField(max_length=240)
    bio = forms.CharField(max_length=300)
    picture = forms.ImageField()
