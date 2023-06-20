from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from loginApp.forms import UserRegisterForm, UserEditForm, ProfileEditForm, AvatarForm
from django.dispatch import receiver
from loginApp.models import Avatar, Profile


# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register/register.html'
    success_url = reverse_lazy('Login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Autentica al usuario recien registrado
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)
        # Loguea al usuario recien registrado
        profile = Profile.objects.create(user=user)
        # Crea un perfil al usuario registrado y luego redirecciona a Editar el perfil
        return redirect('Edit_Profile')

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/register/login.html'
    success_url = reverse_lazy('Home')
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/register/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        avatar = Avatar.objects.filter(user=self.request.user).first()
        context['url'] = avatar.imagen.url
        context['profile'] = profile
        return context
    
class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileEditForm(instance=profile)
        avatar = Avatar.objects.filter(user=request.user).first()
        avatar_form = AvatarForm(instance=avatar)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'avatar_form': avatar_form
        }
        return render(request, 'accounts/register/editprofile.html', context)

    def post(self, request):
        user_form = UserEditForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileEditForm(request.POST, instance=profile)
        avatar = Avatar.objects.filter(user=request.user).first()
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if user_form.is_valid() and profile_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            profile_form.save(commit=False)
            profile_form.instance.user = request.user
            profile_form.save()

            if avatar_form.cleaned_data.get('imagen', None):
                avatar = avatar_form.save(commit=False)
                avatar.user = request.user
                avatar.save()

            return redirect('Home')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'avatar_form': avatar_form
        }
        return render(request, 'accounts/register/editprofile.html', context)
    
