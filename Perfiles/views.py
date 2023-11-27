from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from Perfiles.forms import UserRegisterForm, UserUpdateForm

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


def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user: #chequeo si existe usuario
               login(request=request, user=user) #crea sesion al usuario
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='Perfiles/login.html',
       context={'form': form},
   )



class CustomLogoutView(LogoutView):
    template_name= 'Perfiles/logout.html'
    
    
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'Perfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user