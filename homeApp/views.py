from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from loginApp.models import Avatar


# Create your views here.

class CustomContextAvatarMixin: #Trae el objeto Avatar a todas las clases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user=self.request.user).first()
        context['url'] = avatar.imagen.url
        return context

class HomeView(LoginRequiredMixin, CustomContextAvatarMixin, TemplateView):
    template_name = 'home/home.html'