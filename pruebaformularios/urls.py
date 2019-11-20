from django.urls import path, include
#from django.conf.urls import url
#from pruebaformularios.views import index, persona_view
from . import views


app_name = 'pruebaformularios'
urlpatterns = [
    path('formulario/', views.index, name='mi_form'),
    path('', views.ventana, name='ventana'),
    path('mens/', views.hombre, name='hombre'),
    
]
