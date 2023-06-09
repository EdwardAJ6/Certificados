from django.db import models
from django.contrib.auth.models import AbstractUser

TIPODOC_CHOICES =(
    ("C.C", "'Cédula de ciudadanía"),
    ("T.I", "Tarjeta de identidad"),
)


#Esta es la tabla que se está usando para las PQRS 
class User(AbstractUser):
   cedula = models.PositiveBigIntegerField()
   telefono = models.CharField(max_length=20, blank=True, null=True,verbose_name="Telefono")
   tipoDoc = models.CharField(max_length=50,choices=TIPODOC_CHOICES,blank=True, null=True,verbose_name="Tipo de documento")
   primer_apellido = models.CharField(max_length=50,blank=True, null=True,verbose_name="Primer Apellido")
   segundo_apellido = models.CharField(max_length=50, blank=True, null=True,verbose_name="Segundo Apellido")     


   def get_full_name(self):
     return '{} {}'.format(self.first_name, self.segundo_apellido) 
   