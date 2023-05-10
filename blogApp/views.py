from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from loginApp.models import Avatar
from .custom_filters import zip_lists
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user=self.request.user).first()
        context['url'] = avatar.imagen.url
        return context

def blog(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, 'agenda/blog.html', {'url':avatares[0].imagen.url})

#####

def blogpost(request):
    url = 'https://www.formula1.com/en/drivers.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page.request.url)

    eq = soup.find_all('span', class_='d-block f1--xxs f1-color--carbonBlack')
    nombres = [i.text for i in eq]
    
    eq = soup.find_all('span', class_='d-block f1-bold--s f1-color--carbonBlack')
    apellidos = [i.text for i in eq]

    eq = soup.find_all('div', class_='f1-wide--s')
    puntos = [i.text for i in eq]

    eq = soup.find_all('p', class_='listing-item--team f1--xxs f1-color--gray5')
    equipos = [i.text for i in eq]

    context = {
        'nombre':nombres,
        'apellido':apellidos,
        'punto':puntos,
        'equipo':equipos
    }
    
    return render (request, 'agenda/blog-post.html', context=context)



####

def portfolio(request):

    return render (request, 'agenda/portfolio-post.html')

