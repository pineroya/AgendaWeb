from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from homeApp.views import CustomContextAvatarMixin
from agendaApp.models import AgendaModel
from agendaApp.forms import agendaForm
from django.db.models import Q

# Create your views here.

class ContactList(LoginRequiredMixin, CustomContextAvatarMixin, ListView):
    model = AgendaModel
    template_name = "agenda/contact_list.html"
    context_object_name = 'contacts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return AgendaModel.objects.filter(
                Q(name__icontains=query) | Q(last_name__icontains=query)
            )
        return AgendaModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ContactDetail(CustomContextAvatarMixin, DetailView):
    model = AgendaModel
    template_name = 'agenda/contact_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ContactCreation(LoginRequiredMixin, CustomContextAvatarMixin, CreateView):
    model = AgendaModel
    form_class = agendaForm
    template_name = 'agenda/contact_form.html'
    success_url = reverse_lazy('contact:list')

class ContactUpdate(CustomContextAvatarMixin, UpdateView):
    model = AgendaModel
    template_name = 'agenda/contact_form.html'
    fields = ['name', 'last_name', 'tel_number', 'addres', 'email', 'web', 'bio', 'picture']
    success_url = reverse_lazy('contact:list')

class ContactDelete(CustomContextAvatarMixin, DeleteView):
    model = AgendaModel
    template_name = 'agenda/agendamodel_confirm_delete.html'
    success_url = reverse_lazy('contact:list')