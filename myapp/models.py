from email.policy import default
from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.nombre

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    realizado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + ' - ' + self.proyecto.nombre

    

