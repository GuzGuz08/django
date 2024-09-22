from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeServicios),
    path('registrarServicios/',views.registrarServicios),
    path('eliminarServicio/<Codigo_Servicio>', views.eliminarServicio),
    path('editarServicio/<Codigo_Servicio>', views.editarServicio),
    path('edicionServicio/', views.edicionServicio),
]