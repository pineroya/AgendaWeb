from contactoApp.forms import ContactoForm

def contactanos_form(request):
    return {'contactanos_form': ContactoForm()}
