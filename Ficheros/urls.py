
from django.urls import path

from Ficheros.views import  listar_autos, listar_motos, listar_clientes, crear_clientes, crear_autos, crear_motos



urlpatterns = [
    path("autos/", listar_autos, name="lista_autos"),
    path("motos/", listar_motos, name="lista_motos"),
    path("clientes/", listar_clientes, name="lista_clientes"),
    path("crear-clientes/", crear_clientes, name="crear_cleintes"),
    path("crear-autos/", crear_autos, name="crear_autos"),
    path("crear-motos/", crear_motos, name="crear_motos"),
    
   
    
    
    
   
   
    
]