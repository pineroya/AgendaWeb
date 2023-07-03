"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from .views import *
from notasApp import views
from django.conf import settings

app_name = 'notas'
urlpatterns = [
    path('notas', NotasList.as_view(), name = 'list'),
    url(r'^formulario_nota$', NotaForm.as_view(), name='notaform'),
    url(r'^detail(?P<pk>\d+)$', NotaDelete.as_view(), name='detail'),
    url(r'^edit(?P<pk>\d+)$', NotaUpdate.as_view(), name='edit'),
    url(r'^delete(?P<pk>\d+)$', NotaDelete.as_view(), name='delete'),
    path('categorias/', CategoriaListView.as_view(), name='categorias')
]