from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
from datetime import datetime


# Create your views here.

def agregar_familiares(request, nombre, apellido, edad, fecha):

    familiar = Familiar(nombre = nombre, apellido = apellido, edad = edad)
    fnac = datetime.strptime(fecha, '%Y-%m-%d').date()
    familiar.fnac = fnac
    familiar.save()

    return HttpResponse(f"""
        <p>Nombre: {familiar.nombre} {familiar.apellido} - agregado! </p>
        """)
    
def listar_familiares(request):
    
    lista = Familiar.objects.all()
    
    return render(request, 'familiares.html', {'lista_familiares':lista})