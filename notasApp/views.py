from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from homeApp.views import CustomContextAvatarMixin
from notasApp.forms import NotasForm
from .models import NotasModel, CategoriaNotasModel


# Create your views here.

class NotasList(LoginRequiredMixin, CustomContextAvatarMixin, ListView):
    model = NotasModel
    template_name = 'notas/notas_list.html'
    context_object_name = 'listanotas'

class NotaForm(LoginRequiredMixin, CustomContextAvatarMixin, CreateView):
    model = NotasModel
    form_class = NotasForm
    template_name = 'notas/nota_form.html'
    success_url = reverse_lazy('notas:list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class NotaUpdate(CustomContextAvatarMixin, UpdateView):
    model = NotasModel
    template_name = 'notas/nota_form.html'
    fields = ['titulo', 'camponota','fecha_edicion']
    success_url = reverse_lazy('contact:list')

class NotaDelete(CustomContextAvatarMixin, DeleteView):
    model = NotasModel
    template_name = 'notas/nota_confirm_delete.html'
    success_url = ('contact:list')

class CategoriaListView(CustomContextAvatarMixin, ListView):
    model = CategoriaNotasModel
    template_name = 'notas/categorias.html'
    context_object_name = 'categorias'