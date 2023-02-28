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

class ContactDetail(DetailView):
    model = AgendaModel
    template_name = 'agenda/contact/contact_detail.html'

class ContactCreation(CreateView): #/new/ no funciona
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

#templateview para projects, luego hacer su propia app

