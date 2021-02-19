from django.db import models

# Create your models here.

class Estudiante(models.Model):

    listaGenero = (
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino')
    )

    estudiante_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    genero = models.CharField(choices = listaGenero, default = "femenino", max_length = 30)
    correo = models.EmailField(max_length = 100, null = False)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.cedula


class Materia(models.Model):
    materia_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    modulos = models.IntegerField(default = None)
    date_created = models.DateTimeField(auto_now_add = True)


class Nota(models.Model):
    nota_1 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    nota_2 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    nota_3 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)