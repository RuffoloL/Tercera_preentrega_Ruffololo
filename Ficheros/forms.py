from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    apellido = forms.CharField(required=True, max_length=100)
    email = forms.EmailField()
    
    
class AutoFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=100)
    modelo = forms.CharField(required=True, max_length=100)
    año = forms.IntegerField(required=True, max_value=2023)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    

class MotoFormulario(forms.Form):
    marca = forms.CharField(required=True, max_length=100)
    modelo = forms.CharField(required=True, max_length=100)
    año = forms.IntegerField(required=True, max_value=2023)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    
