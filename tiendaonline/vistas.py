from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def registro(request):

    return render(request, "persona/registro.html")


