from django.urls import include, path
from django.conf.urls import url
from blogApp.views import EntradasDia, EntradasMes, EntradasYear
from blogApp import views
from .views import CalendarView
from django.conf import settings

urlpatterns = [
    path('blog/', views.blog, name = 'Blog'),
    path('blogpost/', views.blogpost, name = 'Blogpost'),
    path('portfolio/', views.portfolio, name = 'Portfolio'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', EntradasDia.as_view(), name='entradas'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$', EntradasMes.as_view(), name='entradas'),
    url(r'^blog/(?P<year>\d{4})/$', EntradasYear.as_view(), name='entradas'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url('bloglist', CalendarView.as_view(), name='listaentrada'),
]