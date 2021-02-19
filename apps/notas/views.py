
from django.db.models import Q  

from .forms import FormularioNota
from django.shortcuts import render
from apps.modelo.models import Estudiante, Materia, Nota
from apps.gestion_estudiantes.forms import FormularioMateria, FormularioEstudiante
from django.shortcuts import render, redirect

def index(request):
    # manejo del ORM
    listaEstudiantes = Estudiante.objects.all()
    return render(request, 'notas/index.html', locals())

def getMateria(request, cedula):
    # manejo del ORM
    listaMaterias = Materia.objects.all()
    return render(request, 'notas/getMateria.html', locals())

def getNotas(request, cedula, materia):
    formulario_nota = FormularioNota()
    if request.method == 'POST':
        if formulario_nota.is_valid():
            nota = Nota()
            datos_nota = formulario_nota.cleaned_data
            estudiante = Estudiante.objects.get(cedula=cedula)
            materia = Materia.objects.get(materia_id = materia)
            materia.nota_1 = datos_nota.get('nota_1')
            materia.nota_2 = datos_nota.get('nota_2')
            materia.nota_2 = datos_nota.get('nota_3')
            # ORM
            materia.save()
            return redirect(Mensaje)
    return render(request, 'notas/notas.html', locals())

def Mensaje(request, nota1, nota2, nota3):
    notaFinal = nota1+nota2+nota3
    if (notaFinal > 7):
        mensaje = "Pasaste"
    else :
        mensaje = "No pasaste"    
    return render(request, 'notas/mesaje.html', locals())
