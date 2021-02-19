
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="notas"),
    path('estudiante/<int:cedula>/', views.getMateria, name="estudiante_materia"),
    path('calcularNota/<int:cedula>/<int:materia>', views.getNotas, name="calcularNota"),
    path('mensaje/<int:nota1>/<int:nota2>/<int:nota3>', views.Mensaje, name="mensaje"),
]