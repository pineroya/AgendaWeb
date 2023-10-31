from django.core.mail import EmailMessage
from django.views.generic import FormView, TemplateView
from .forms import ContactoForm
from django.urls import reverse_lazy
from homeApp.views import CustomContextAvatarMixin
from django.shortcuts import render

#Create your views here.

class ContactanosView(FormView):
    template_name = "base.html"
    form_class = ContactoForm
    success_url = '/contacto_exito/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']
        fecha = form.cleaned_data['fecha'] #no está en uso todavia

        # Lógica para enviar el correo
        email = EmailMessage(
            "Mensaje desde 'El Cuaderno'",
            "Usuario con la dirección {}, escribe lo siguiente:\n\nAsunto: {}\n\n{}".format(email, mensaje, fecha),
            "", ["mispruebas.yam@gmail.com"],
            reply_to=[email]
        )
        email.send()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contactanos_form'] = self.get_form()
        return context

class Contacto_exito(CustomContextAvatarMixin, TemplateView):
    template_name = 'contacto/contacto_exito.html'
