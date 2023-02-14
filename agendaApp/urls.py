"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from agendaApp.views import ContactCreation, ContactDelete, ContactList, ContactDetail, ContactUpdate
from django.conf import settings

app_name = 'contact'
urlpatterns = [
    url(r'^list', ContactList.as_view(), name='list'),
    url(r'^list(?P<pk>\d+)$', ContactDetail.as_view(), name='detail'),
    url(r'^new$', ContactCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ContactUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ContactDelete.as_view(), name='delete'),
]