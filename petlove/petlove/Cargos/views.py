from django.shortcuts import render, redirect
from .models import Cargos
from django.contrib import messages

# Create your views here.

def home(request):
    Cargoslista = Cargos.objects.all() #todos los Cargos
    messages.success(request, '!Cargos listados¡')
    return render(request,"gestioncargos.html", {"Cargos": Cargoslista})

def registrarCargo(request):
    ID = request.POST['ID']
    Descripcion = request.POST['txtdescripcion']

    Cargo=Cargos.objects.create(Codigo_Cargo_id = ID, Descripcion = Descripcion )
    messages.success(request, '!Cargo registrado¡')
    return redirect('/')

def eliminarCargo(request, Codigo_Cargo_id):
    cargo = Cargos.objects.get(Codigo_Cargo_id = Codigo_Cargo_id)
    cargo.delete()
    messages.success(request, '!Cargo Eliminado¡')
    return redirect('/')

def editarCargo(request,Codigo_Cargo_id):
    cargo = Cargos.objects.get(Codigo_Cargo_id = Codigo_Cargo_id)
    return render(request, "editarCargo.html", {"cargo":cargo})

def edicionCargo(request):
    ID = request.POST['ID']
    Descripcion = request.POST['txtdescripcion']

    cargo = Cargos.objects.get(Codigo_Cargo_id = ID )
    cargo.Descripcion = Descripcion
    cargo.save()
    messages.success(request, '!Cargo actualizado¡')
    return redirect('/')



