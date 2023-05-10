from django.shortcuts import render
from requests import request
from loginApp.models import Avatar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import ContactoForm

# Create your views here.

class ContactoView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar = Avatar.objects.filter(user=self.request.user).first()
        context['url'] = avatar.imagen.url
        return context

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # handle invalid form data here
            pass

        return render(request, 'contacto.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = ContactoForm()
        return render(request, 'contacto/contacto.html', {'form': form})
