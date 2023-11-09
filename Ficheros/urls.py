
from django.urls import path

from Ficheros.views import  listar_autos, listar_motos, listar_clientes



urlpatterns = [
    path("autos/", listar_autos, name="lista_autos"),
    path("motos/", listar_motos, name="lista_motos"),
    path("clientes/", listar_clientes, name="lista_clientes"),
    
   
    
    
    
   
   
    
]