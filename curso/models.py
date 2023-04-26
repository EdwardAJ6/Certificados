from django.db import models
from django.utils import timezone
from usuario.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()

    

    def __str__(self) :
        return self.nombre
    

class Etapa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    finalizado = models.BooleanField(default=False)
    fechaInicio =  models.DateTimeField()
    fechaFin = models.DateTimeField()
    orden = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='etapas', null=True, default=None)

    def __str__(self):
        return self.nombre


class Progreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)
    aprobado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('usuario', 'curso', 'etapa')
