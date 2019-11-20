from django.shortcuts import render, redirect
from .models import Persona
from .forms import RegistrarUsuario
from django.contrib.messages import success
from django.db import models
from django.http import HttpResponseRedirect

def index(request):

    #mis_usuarios = obj.objects.all()
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            obj = Persona()
            obj.nombre = form.cleaned_data['nombre']                                                            
            obj.apellidos = form.cleaned_data['apellidos']
            obj.direccion = form.cleaned_data['direccion']
            obj.email = form.cleaned_data['email']

            obj.save()

            return redirect('/')
    else:
        register_form = RegistrarUsuario()
        return render(request, 'forms/formulario.html', {'register_form': register_form}) #'usuarios': mis_usuarios


def ventana(request):
    return render(request, 'forms/inicio.html')

def hombre(request):
    return render(request, 'forms/hombre.html')





"""
register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            register_form.save()"""