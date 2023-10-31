from django import forms
from PIL import Image
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from loginApp.models import Avatar, Profile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

########
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'website_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'contact_field'})
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('imagen', )