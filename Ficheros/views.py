from django.shortcuts import render, redirect
from django.urls import reverse

from Ficheros.forms import ClienteFormulario, AutoFormulario, MotoFormulario

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

#def crear_clientes(request):
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

#def crear_autos(request):
    if request.method == "POST": #request.POST es un diccionario
        #Guardado de datos
        data = request.POST
        #Creo un curso en memoria RAM
        auto = Auto(marca=data['marca'], modelo=data['modelo'], año=data['año'], precio=data['precio'])
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

#def crear_motos(request):
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

def crear_clientes(request):
   if request.method == "POST":
       formulario = ClienteFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           apellido = data["apellido"]
           email = data["email"]
           cliente = Cliente(nombre=nombre, apellido=apellido, email=email)  # lo crean solo en RAM
           cliente.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_clientes')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = ClienteFormulario()
   http_response = render(
       request=request,
       template_name='Ficheros/formulario_clientes1.html',
       context={'formulario': formulario}
   )
   return http_response


def crear_autos(request):
   if request.method == "POST":
       formulario = AutoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           marca = data["marca"]
           modelo = data["modelo"]
           año = data["año"]
           precio = data["precio"]
           auto = Auto(marca=marca, modelo=modelo, año=año, precio=precio)  # lo crean solo en RAM
           auto.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_autos')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = AutoFormulario()
   http_response = render(
       request=request,
       template_name='Ficheros/formulario_autos1.html',
       context={'formulario': formulario}
   )
   return http_response



def crear_motos(request):
   if request.method == "POST":
       formulario = MotoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           marca = data["marca"]
           modelo = data["modelo"]
           año = data["año"]
           precio = data["precio"]
           moto = Moto(marca=marca, modelo=modelo, año=año, precio=precio)  # lo crean solo en RAM
           moto.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_motos')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = MotoFormulario()
   http_response = render(
       request=request,
       template_name='Ficheros/formulario_motos1.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_clientes(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       clientes = Cliente.objects.filter(apellido__contains=busqueda)
       contexto = {
           "clientes": clientes,
       }
       http_response = render(
           request=request,
           template_name='Ficheros/lista_clientes.html',
           context=contexto,
       )
       return http_response
   
def buscar_autos(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       autos = Auto.objects.filter(marca__contains=busqueda)
       contexto = {
           "autos": autos,
       }
       http_response = render(
           request=request,
           template_name='Ficheros/lista_autos.html',
           context=contexto,
       )
       return http_response
   

def buscar_motos(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       motos = Moto.objects.filter(marca__contains=busqueda)
       contexto = {
           "motos": motos,
       }
       http_response = render(
           request=request,
           template_name='Ficheros/lista_motos.html',
           context=contexto,
       )
       return http_response
   

def eliminar_auto(request, id):
    # obtienes el auto de la BD
   auto = Auto.objects.get(id=id)
   if request.method == "POST":
       #borra el auto de la BD
       auto.delete()
       #redireccionamos a la URL exitosa
       url_exitosa = reverse('lista_autos')
       return redirect(url_exitosa)
   
def eliminar_moto(request, id):
    # obtienes la moto de la BD
   moto = Moto.objects.get(id=id)
   if request.method == "POST":
       #borra la moto de la BD
       moto.delete()
       #redireccionamos a la URL exitosa
       url_exitosa = reverse('lista_motos')
       return redirect(url_exitosa)