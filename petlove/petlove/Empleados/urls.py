from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeempleados),
    path('registrarEmpleado/',views.registrarEmpleado),
    path('eliminarEmpleado/<Codigo_Empleado>', views.eliminarEmpleado),
    path('editarEmpleado/<Codigo_Empleado>', views.editarEmpleado),
    path('edicionEmpleado/', views.edicionEmpleado),
]