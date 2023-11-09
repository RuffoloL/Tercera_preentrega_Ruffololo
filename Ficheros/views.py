from django.shortcuts import render
from Ficheros.models import Auto, Moto, Cliente

def saludo_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response



def listar_autos(request):
    contexto ={
        "autos" : Auto.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Ficheros/lista_autos.html',
        context=contexto,     
    )
    return http_response


def listar_motos(request):
    contexto ={
        "motos" : Moto.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Ficheros/lista_motos.html',
        context=contexto,     
    )
    return http_response


def listar_clientes(request):
    contexto ={
        "clientes" : Cliente.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Ficheros/lista_clientes.html',
        context=contexto,     
    )
    return http_response