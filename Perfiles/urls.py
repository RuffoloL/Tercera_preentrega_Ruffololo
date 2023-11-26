from django.contrib import admin
from django.urls import path

from Perfiles.views import registro


urlpatterns = [
   # URLS Usuario y sesion
   path('registro/', registro, name="registro"),
]
