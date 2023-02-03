from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from loginApp.models import Avatar
from .models import AgendaModel
from .forms import agendaForm

# Create your views here.

def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, "home/home.html", {'url':avatares[0].imagen.url})

def blog(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, 'agenda/blog.html', {'url':avatares[0].imagen.url})

def blogpost(request):

    return render (request, 'agenda/blog-post.html')

# def agenda(request):

#     return render (request, 'agenda/index.html')

def portfolio(request):

    return render (request, 'agenda/portfolio-post.html')

class ContactList(ListView):
    model = AgendaModel
    template_name = "agenda/contact_list.html"

class ContactDetail(DetailView):
    model = AgendaModel

class ContactCreation(CreateView):
    model = AgendaModel
    form_class = agendaForm
    template_name = 'agenda/contact_form.html'
    succes_url = reverse_lazy('contact:list')

class ContactUpdate(UpdateView):
    model = AgendaModel
    success_url = reverse_lazy('contact:list')
    fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']

class ContactDelete(DeleteView):
    model = AgendaModel
    success_url = reverse_lazy('contact:list')

