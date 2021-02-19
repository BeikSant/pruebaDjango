from django.shortcuts import render
from apps.modelo.models import Estudiante, Materia
from .forms import FormularioMateria, FormularioEstudiante
from django.shortcuts import render, redirect


def index(request):
    # manejo del ORM
    listaEstudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/index.html', locals())


def crearEstudiante(request):
    formulario_estudiante = FormularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario_estudiante.is_valid():
            estudiante = Estudiante()
            datos_estudiante = formulario_estudiante.cleaned_data
            estudiante.cedula = datos_estudiante.get('cedula')
            estudiante.nombres = datos_estudiante.get('nombres')
            estudiante.apellidos = datos_estudiante.get('apellidos')
            estudiante.genero = datos_estudiante.get('genero')
            estudiante.correo = datos_estudiante.get('correo')
            # ORM
            estudiante.save()
        return redirect(index)
    return render(request, 'estudiantes/crear.html', locals())


def modificarEstudiante(request, cedula):
    estudiante = Estudiante.objects.get(cedula=cedula)
    if request.method == 'GET':
        formulario_estudiante = FormularioEstudiante(instance=estudiante)
    else:
        formulario_estudiante = FormularioEstudiante(
            request.POST, instance=estudiante)
        if formulario_estudiante.is_valid():
            # ORM
            formulario_estudiante.save()
        return redirect(index)
    return render(request, 'estudiantes/modificar.html', locals())


def eliminarEstudiante(request, cedula):
    estudiante = Estudiante.objects.get(cedula=cedula)
    estudiante.delete()
    return redirect(index)


def materias(request):
    # manejo del ORM
    listaMaterias = Materia.objects.all()
    return render(request, 'materias/index.html', locals())


def crearMateria(request):
    formulario_materia = FormularioMateria(request.POST)
    if request.method == 'POST':
        if formulario_materia.is_valid():
            materia = Materia()
            datos_materia = formulario_materia.cleaned_data
            materia.nombre = datos_materia.get('nombre')
            materia.modulos = datos_materia.get('modulos')
            # ORM
            materia.save()
        return redirect(materias)
    return render(request, 'materias/crear.html', locals())
# Create your views here.
