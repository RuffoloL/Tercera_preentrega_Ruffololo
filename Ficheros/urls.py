
from django.urls import path

from Ficheros.views import  (
    listar_autos, listar_motos, listar_clientes, crear_clientes, crear_autos, crear_motos,
    buscar_clientes, buscar_autos, buscar_motos, eliminar_cliente, eliminar_auto, eliminar_moto,
    editar_auto, editar_moto, editar_cliente
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
    path("eliminar-cliente/<int:id>/", eliminar_cliente, name="eliminar_cliente"),
    path("eliminar-auto/<int:id>/", eliminar_auto, name="eliminar_auto"),
    path("eliminar-moto/<int:id>/", eliminar_moto, name="eliminar_moto"),
    path("editar-auto/<int:id>/", editar_auto, name="editar_auto"),
    path("editar-moto/<int:id>/", editar_moto, name="editar_moto"),
    path("editar-cliente/<int:id>/", editar_cliente, name="editar_cliente"),
    
    
    
    
   
   
    
]