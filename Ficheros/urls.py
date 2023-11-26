
from django.urls import path

from Ficheros.views import  (
    listar_autos, listar_motos, listar_clientes, crear_clientes, crear_autos, crear_motos,
    buscar_clientes, buscar_autos, buscar_motos, eliminar_auto, eliminar_moto
)    

  

urlpatterns = [
    path("autos/", listar_autos, name="lista_autos"),
    path("motos/", listar_motos, name="lista_motos"),
    path("clientes/", listar_clientes, name="lista_clientes"),
    path("crear-clientes/", crear_clientes, name="crear_clientes"),
    path("crear-autos/", crear_autos, name="crear_autos"),
    path("crear-motos/", crear_motos, name="crear_motos"),
    path("buscar-clientes/", buscar_clientes, name="buscar_clientes"),
    path("buscar-autos/", buscar_autos, name="buscar_autos"),
    path("buscar-motos/", buscar_motos, name="buscar_motos"),
    path("eliminar-auto/<int:id>/", eliminar_auto, name="eliminar_auto"),
    path("eliminar-moto/<int:id>/", eliminar_moto, name="eliminar_moto"),
    
    
    
    
   
   
    
]