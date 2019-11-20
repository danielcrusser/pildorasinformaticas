from django import forms
from datetime import datetime

from pruebaformularios.models import Persona

class RegistrarUsuario(forms.Form):
    
    nombre = forms.CharField(label='Nombre:', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre',}))                                                                    
    apellidos = forms.CharField(label='Apellidos', max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'apellido',}))
    direccion = forms.CharField(label='direccion', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'4567876',}))
    email = forms.EmailField(label='email', max_length=254, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'elmer.hack@heckmail.com',}))


def registrar_usuario(self):
        
        nuevo_usuario = Persona(nombre=self.data['nombre'],
                        apellidos=self.data['apellidos'],
                        direccion=self.data['direccion'],
                        email=self.data['email'])
        nuevo_usuario.save()
        return 'Registro exitoso'

