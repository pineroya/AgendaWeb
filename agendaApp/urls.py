"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from agendaApp.views import home, blog, blogpost, portfolio, ContactCreation, ContactDelete, ContactList, ContactDetail, ContactUpdate 
from django.conf import settings

urlpatterns = [
    path('', home, name = 'Home'),
    path('blog/', blog, name = 'Blog'),
    path('blogpost/', blogpost, name = 'Blogpost'),
    path('portfolio/', portfolio, name = 'Portfolio'),
    url(r'^list', ContactList.as_view(), name='list'),
    url(r'^list(?P<pk>\d+)$', ContactDetail.as_view(), name='detail'),
    url(r'^nuevo$', ContactCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ContactUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ContactDelete.as_view(), name='delete'),
]