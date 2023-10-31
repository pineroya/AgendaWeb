from django.urls import include, path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'Home'),
]