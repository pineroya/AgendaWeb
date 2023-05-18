"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from .views import ContactanosView
from django.conf import settings

urlpatterns = [
    path('contactanos/', ContactanosView.as_view(), name = 'Contactanos'),
]