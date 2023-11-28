from django.test import TestCase

from Ficheros.models import Cliente, Auto, Moto



class ClienteTests(TestCase):
   """En esta clase van todas las pruebas del modelo Cliente."""

   def test_creacion_cliente(self):
       # caso uso esperado
       cliente = Cliente(nombre="texto", apellido="texto", email="example@example.com")
       cliente.save()

       # Compruebo que el cliente fue creado y la data fue guardad correctamente
       self.assertEqual(Cliente.objects.count(), 1)
       self.assertEqual(cliente.nombre, "texto")
       self.assertEqual(cliente.apellido, "texto")
       self.assertEqual(cliente.email, "example@example.com")

   def test_cliente_str(self):
       cliente = Cliente(nombre="Juan", apellido="Perez")
       cliente.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(cliente.__str__(), "Juan, Perez")


class AutoTests(TestCase):
   """En esta clase van todas las pruebas del modelo Auto."""

   def test_creacion_Auto(self):
       # caso uso esperado
       auto = Auto(marca="texto", modelo="texto", año=1000, precio=10000000)
       auto.save()

       # Compruebo que el auto fue creado y la data fue guardad correctamente
       self.assertEqual(Auto.objects.count(), 1)
       self.assertEqual(auto.marca, "texto")
       self.assertEqual(auto.modelo, "texto")
       self.assertEqual(auto.año, 1000)
       self.assertEqual(auto.precio, 10000000)
       
def test_auto_str(self):
       auto = Auto(marca="Fiat", modelo="Cronos", año=2020, precio=23000000)
       auto.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(str(self.auto), "Fiat, Cronos, 2020, $23000000")

      

class MotoTests(TestCase):
   """En esta clase van todas las pruebas del modelo Moto."""

   def test_creacion_moto(self):
       # caso uso esperado
       moto = Moto(marca="texto", modelo="texto", año=1000, precio=10000000)
       moto.save()

       # Compruebo que el auto fue creado y la data fue guardad correctamente
       self.assertEqual(Moto.objects.count(), 1)
       self.assertEqual(moto.marca, "texto")
       self.assertEqual(moto.modelo, "texto")
       self.assertEqual(moto.año, 1000)
       self.assertEqual(moto.precio, 10000000)
       
def test_moto_str(self):
       moto = Moto(marca="Suzuki", modelo="Rmz", año=2014, precio=7950000)
       moto.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(str(self.moto), "Suzuki, Rmz, 2014, $7950000")