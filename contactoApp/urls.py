"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import path
from django.conf.urls import url
from .views import ContactanosView, Contacto_exito

urlpatterns = [
    path('contactanos/', ContactanosView.as_view(), name = 'Contactanos'),
    path('contacto_exito/', Contacto_exito.as_view(), name='Contacto_exito'),
]