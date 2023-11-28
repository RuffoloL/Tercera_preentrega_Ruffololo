# PoryectoFicheros
Comision: 47780
Alumno: Ruffolo Luciano

## Instrucciones instalar proyecto en local
+ Crea una carpeta madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyercto en la carpeta madre
+ Entra en la carpeta que acabas de clonar 
+ Para instalar dependencias corre este comando :


``` pip install -r requirements.txt
```
## Instrucciones para entrar al panel administrativo
+ En consola, crear superuser:

``` python manage.py createsuperuser
```
Acceder con user y password via:

``` http://127.0.0.1:8000/admin/
```
Usuario: luciano
password: 1234abcd


Acceso a clientes /ficheros/clientes/
         autos /ficheros/autos/
         motos / ficheros motos/

de igual forma podemos acceder a la carga de los mismos 

ficheros/crear-clientes/
        /crear-autos/
        /crear-motos/

Mediante la siguiente ruta tenemos acceso a todo lo que es la app de perfiles 

perfiles/login
perfiles/logout
perfiles/registro
perfiles/editar-mi-perfil

tendremos acceso a todo siempre y cuando seamos un usuario registrado e iniciemos sesion, de lo contrario solo podremos ver algunas cosas,
como por ejemplo el hompage (inicio), lista de autos y motos cargados en sistema, pero no podremos visualizar la lista de clientes por ejemplo y mucho menos tratar de editar o borrar algun objeto ya cargado en la BD.

## Test Units:

"Ficheros/tests.py"

+ En terminal, correr:

``` python manage.py test
```


        