from django.shortcuts import render, redirect
from django.urls import reverse
from Ficheros.models import Auto, Moto, Cliente


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

def crear_clientes(request):
    if request.method == "POST": #request.POST es un diccionario
        #Guardado de datos
        data = request.POST
        #Creo un curso en memoria RAM
        cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'])
        # .save lo guarda en la base de datos
        cliente.save()
        #Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_clientes')
        return redirect(url_exitosa)
    else: #GET
        #Descarga formulario inicial
            http_response = render(
            request=request,
            template_name='Ficheros/formulario_clientes.html',
    )
    return http_response

def crear_autos(request):
    if request.method == "POST": #request.POST es un diccionario
        #Guardado de datos
        data = request.POST
        #Creo un curso en memoria RAM
        auto = Auto(nombre=data['marca'], apellido=data['modelo'], año=data['año'], precio=data['precio'])
        # .save lo guarda en la base de datos
        auto.save()
        #Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_autos')
        return redirect(url_exitosa)
    else: #GET
        #Descarga formulario inicial
            http_response = render(
            request=request,
            template_name='Ficheros/formulario_autos.html',
    )
    return http_response

def crear_motos(request):
    if request.method == "POST": #request.POST es un diccionario
        #Guardado de datos
        data = request.POST
        #Creo un curso en memoria RAM
        moto = Moto(marca=data['marca'], modelo=data['modelo'], año=data['año'], precio=data['precio'])
        # .save lo guarda en la base de datos
        moto.save()
        #Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_motos')
        return redirect(url_exitosa)
    else: #GET
        #Descarga formulario inicial
            http_response = render(
            request=request,
            template_name='Ficheros/formulario_motos.html',
    )
    return http_response