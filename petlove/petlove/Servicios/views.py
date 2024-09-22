from django.shortcuts import render, redirect
from .models import Servicios
from django.contrib import messages

# Create your views here.

def homeServicios(request):
    Servicioslista = Servicios.objects.all() #todos los empleados
    messages.success(request, '!Servicios listados¡')
    return render(request,"gestionServicios.html", {"servicios": Servicioslista})

def registrarServicios(request):
    ID = request.POST['ID']
    Nombre = request.POST['nombre']
    Precio = request.POST['precio']
    Descripcion =request.POST['descripcion']

    servicio=Servicios.objects.create(Codigo_Servicio = ID, Nombre = Nombre,Precio=Precio,Descripcion=Descripcion)
    messages.success(request, '!Servicio registrado¡')
    return redirect('/')

def eliminarServicio(request, Codigo_Servicio):
    servicio = Servicios.objects.get(Codigo_Servicio = Codigo_Servicio)
    servicio.delete()
    messages.success(request, '!Servicio Eliminado¡')
    return redirect('/')

def editarServicio(request,Codigo_Servicio):
    Servicio = Servicios.objects.get(Codigo_Servicio = Codigo_Servicio)
    return render(request, "editarServicio.html", {"servicio":Servicio})

def edicionServicio(request):
    ID = request.POST['ID']
    Nombre = request.POST['nombre']
    Precio = request.POST['precio']
    Descripcion =request.POST['descripcion']
    

    Servicio = Servicios.objects.get(Codigo_Servicio = ID )
    Servicio.Nombre = Nombre
    Servicio.Precio = Precio
    Servicio.Descripcion = Descripcion
    
    Servicio.save()
    messages.success(request, '!Servicio actualizado¡')
    return redirect('/')



