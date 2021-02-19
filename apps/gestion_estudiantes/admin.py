from django.contrib import admin


from apps.modelo.models import Materia
from apps.modelo.models import Estudiante


admin.site.register(Estudiante)
admin.site.register(Materia)
# Register your models here.
