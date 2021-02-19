from django import forms

from apps.modelo.models import Nota

class FormularioNota(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["nota_1","nota_2","nota_3"]