from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCargo/',views.registrarCargo),
    path('eliminarCargo/<Codigo_Cargo_id>', views.eliminarCargo),
    path('editarCargo/<Codigo_Cargo_id>', views.editarCargo),
    path('edicionCargo/', views.edicionCargo),
]