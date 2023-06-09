from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from loginApp.models import Avatar
from .models import AgendaModel
from .forms import agendaForm

# Create your views here.

class ContactList(ListView):
    model = AgendaModel
    template_name = "agenda/contact/contact_list.html"
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user=self.request.user).first()
        context['url'] = avatar.imagen.url
        return context

class ContactDetail(DetailView): #no lleva al detalle del contacto seleccionado, solo actualiza la lista
    model = AgendaModel
    template_name = 'agenda/contact/contact_detail.html'
    def get_object(self, queryset=None):
        # Obtiene el objeto de modelo específico basado en el parámetro 'pk' de la URL
        return self.model.objects.get(pk=self.kwargs['pk'])

class ContactCreation(CreateView):
    model = AgendaModel
    form_class = agendaForm
    template_name = 'agenda/contact/contact_form.html'
    success_url = reverse_lazy('contact:list')

class ContactUpdate(UpdateView):
    model = AgendaModel
    template_name = 'agenda/contact/contact_form.html'
    fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']
    success_url = reverse_lazy('contact:list')

class ContactDelete(DeleteView):
    model = AgendaModel
    template_name = 'agenda/contact/agendamodel_confirm_delete.html'
    success_url = reverse_lazy('contact:list')