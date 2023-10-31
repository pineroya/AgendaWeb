from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DayArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from loginApp.models import Avatar
from .custom_filters import zip_lists
import requests
import pandas as pd
from bs4 import BeautifulSoup
from django.db.models import Q
from django import template
from datetime import date, timedelta
from blogApp.models import CalendarioModel

# Create your views here.

def blog(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, 'blog/blog.html', {'url':avatares[0].imagen.url})

# agregar la lista del modelo Entrada en el template de blog

def portfolio(request):

    return render (request, 'blog/portfolio-post.html')

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
    
    return render (request, 'blog/blog-post.html', context=context)

####

class CalendarView(ListView):
    model = CalendarioModel
    template_name = 'blog/bienvenidos.html'
    context_object_name = 'entradas'

register = template.Library()

# objetos = CalendarioModel.objects.all()

# # Itera a través de los objetos y muestra sus atributos
# for objeto in objetos:
#     print(f'Título: {objeto.titulo}')
#     print(f'Autor: {objeto.autor}')
#     print(f'Texto: {objeto.texto}')
#     print(f'Fecha de Creación: {objeto.fecha_creacion}')
#     print(f'Estado: {objeto.get_estado_display()}')  # Muestra la representación legible del campo 'estado'

# #####

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

def cal_mes(year=date.today().year, month=date.today().month):
    event_list = CalendarioModel.objects.filter(fecha_creacion_year=year, fecha_creacion_month=month)
    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calentar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month - timedelta(7 - last_day_of_month.weekday())

    cal_mes = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calentar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        for event in event_list:
            if day >= event.fecha_creacion.date() and day <= event.fecha_creacion.date():
                cal_day['event'] = True
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if day.weekday() == 6:
            cal_mes.append(week)
            week = []
        i += 1
        day += timedelta(1)
    
    return {'calendar': cal_mes, 'headers': week_headers}

register.inclusion_tag('blog/tags/cal_mes.html')(cal_mes)

class EntradasDia(DayArchiveView):
    queryset = CalendarioModel.objects.order_by('fecha_creacion')
    template_name = 'blog/entradas_dia.html'
    date_field = 'fecha_creacion'
    context_object_name = 'entradas'
    month_format = '%m'

class EntradasMes(MonthArchiveView):
    queryset = CalendarioModel.objects.order_by('fecha_creacion')
    template_name = 'blog/entradas_mes.html'
    date_field = 'fecha_creacion'
    month_format = '%m'
    context_object_name = 'entradas'

class EntradasYear(YearArchiveView):
        queryset=CalendarioModel.objects.order_by('fecha_creacion')
        template_name='blog/entradas_año.html'
        date_field = 'fecha_creacion'
        context_object_name='entradas'
        make_object_list='True'

def buscar(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(Titulo_icontains=query)|
            Q(Texto_icontains=query)
        )
        results = CalendarioModel.objects.filter(qset)
    else:
        results = []
    return render('blog/search.html',{
        "results": results,
        "query": query
    })

