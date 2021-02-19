from django import forms

from apps.modelo.models import Materia, Estudiante

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["cedula","nombres","apellidos","genero","correo"]


class FormularioMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre","modulos"]