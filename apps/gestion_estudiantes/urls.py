from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="estudiantes"),
    path('crearEstudiantes', views.crearEstudiante, name='crear_estudiantes'),
    path('modificarEstudiante/<int:cedula>/', views.modificarEstudiante, name='modificar_estudiante'),
    path('eliminarEstudiante/<int:cedula>/', views.eliminarEstudiante, name='eliminar_estudiante'),

    path('materias', views.materias, name="materias"),
    path('crearMateria', views.crearMateria, name='crear_materia'),

]