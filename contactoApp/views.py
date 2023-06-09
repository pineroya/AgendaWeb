from django.core.mail import EmailMessage
from loginApp.models import Avatar
from django.views.generic import TemplateView, FormView
from .forms import ContactoForm

# Create your views here.

class ContactanosView(FormView):
    template_name = "contacto/contactanos.html"
    form_class = ContactoForm
    success_url = '/contactanos/?valido'

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']
        fecha = form.cleaned_data['fecha']

        # Lógica para enviar el correo
        email = EmailMessage(
            "Mensaje desde 'The Blog'",
            "Usuario {}, con la dirección {}, escribe lo siguiente:\n\n{}".format(nombre, email, mensaje),
            "", ["mispruebas.yam@gmail.com"],
            reply_to=[email]
        )
        email.send()

        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     avatar = Avatar.objects.filter(user=self.request.user).first()
    #     context['url'] = avatar.imagen.url
    #     return context