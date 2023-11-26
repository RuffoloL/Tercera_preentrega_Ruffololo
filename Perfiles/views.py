from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from Perfiles.forms import UserRegisterForm

def registro(request):
   if request.method == "POST":
       #Guardado de datos
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       #Descargar formulario inicial
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='Perfiles/registro.html',
       context={'form': formulario},
   )
