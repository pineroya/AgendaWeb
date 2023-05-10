"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from .views import ContactoView
from django.conf import settings

urlpatterns = [
    path('contacto/', ContactoView.as_view(), name = 'Contacto'),
]