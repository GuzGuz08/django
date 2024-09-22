from django.shortcuts import render, redirect
from .models import Empleados
from django.contrib import messages

# Create your views here.

def homeempleados(request):
    empleadoslista = Empleados.objects.all() #todos los empleados
    messages.success(request, '!Empleados listados¡')
    return render(request,"gestionEmpleados.html", {"empleados": empleadoslista})

def registrarEmpleado(request):
    ID = request.POST['ID']
    Nombre = request.POST['nombre']
    Apellido = request.POST['apellido']
    Telefono =request.POST['telefono']
    Email = request.POST['email']
    Codigo_Cargo_id = request.POST['cargoid']

    empleado=Empleados.objects.create(Codigo_Empleado = ID, Nombre = Nombre,Apellido=Apellido,Telefono=Telefono,Email=Email,Codigo_Cargo_id=Codigo_Cargo_id )
    messages.success(request, '!Empleado registrado¡')
    return redirect('/')

def eliminarEmpleado(request, Codigo_Empleado):
    empleado = Empleados.objects.get(Codigo_Empleado = Codigo_Empleado)
    empleado.delete()
    messages.success(request, '!empleado Eliminado¡')
    return redirect('/')

def editarEmpleado(request,Codigo_Empleado):
    empleado = Empleados.objects.get(Codigo_Empleado = Codigo_Empleado)
    return render(request, "editarEmpleado.html", {"empleado":empleado})

def edicionEmpleado(request):
    ID = request.POST['ID']
    Nombre = request.POST['nombre']
    Apellido = request.POST['apellido']
    Telefono =request.POST['telefono']
    Email = request.POST['email']
    Codigo_Cargo_id = request.POST['cargoid']

    empleado = Empleados.objects.get(Codigo_Empleado = ID )
    empleado.Nombre = Nombre
    empleado.Apellido = Apellido
    empleado.Telefono = Telefono
    empleado.Email = Email
    empleado.Codigo_Cargo_id = Codigo_Cargo_id
    empleado.save()
    messages.success(request, '!Empleado actualizado¡')
    return redirect('/')



