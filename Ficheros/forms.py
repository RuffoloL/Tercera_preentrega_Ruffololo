from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    apellido = forms.CharField(required=True, max_length=100)
    email = forms.EmailField()
    
   
