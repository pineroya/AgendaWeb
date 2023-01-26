import imp
from django.views import generic
from django.core.mail import send_mail
from django.shortcuts import HttpResponse, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from loginApp.forms import UserRegisterForm, UserEditForm, BioWebForm, ContactForm, AvatarForm
from loginApp.models import Avatar, Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            usuario = form.save()
            login(request, usuario)

            return render(request, "home/add_avatar.html")
    else:
        form = UserRegisterForm()
    
    return render(request, "home/registration/register.html", {'form': form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "home/home.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                messages.error(request, 'usuario no válido')
        else:
            messages.error(request, 'información incorrecta')
        
    form = AuthenticationForm()
    return render(request, "home/registration/login.html", {'form': form})

def myProfile(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "home/registration/my_profile.html", {'url':avatares[0].imagen.url})

def editProfile(request):
    usuario = request.user
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion.cleaned_data
            usuario.last_name = informacion.cleaned_data
            usuario.save()

            return render(request, "home/registration/my_profile.html")
    
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "home/registration/editprofile.html", {'miFormulario': miFormulario, 'usuario': usuario, 'url':avatares[0].imagen.url})

def editBW(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        miFormulario = BioWebForm(request.POST)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)
            bioweb = Profile(user=u, bio=miFormulario.cleaned_data['bio'], website_url=miFormulario.cleaned_data['website_url'])
            bioweb.save()

            return render(request, 'home/home.html')
    else:
        miFormulario=BioWebForm()
    return render (request, 'home/registration/editbw.html', {'miFormulario': miFormulario, 'url':avatares[0].imagen.url})

def addAvatar(request):


    if request.method == "POST":

        miFormulario = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render (request, "home/home.html")

    else:

        miFormulario=AvatarForm()

    return render (request, "home/registration/add_avatar.html", {'miFormulario': miFormulario})