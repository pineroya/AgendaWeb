from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from loginApp.models import Avatar
from .models import AgendaModel
from .forms import agendaForm

# Create your views here.

class ContactList(ListView):
    model = AgendaModel
    template_name = "contact/contact_list.html"
    queryset = AgendaModel.objects.all()
    def get_object(self):
        obj = super().get_object()
        return obj

class ContactDetail(DetailView):
    model = AgendaModel

class ContactCreation(CreateView):
    model = AgendaModel
    form_class = agendaForm
    template_name = 'contact/contact_form.html'
    succes_url = reverse_lazy('contact:list')

class ContactUpdate(UpdateView):
    model = AgendaModel
    template_name = 'contact/contact_form.html'
    fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']
    success_url = reverse_lazy('contact:list')

class ContactDelete(DeleteView):
    model = AgendaModel
    success_url = reverse_lazy('contact:list')

