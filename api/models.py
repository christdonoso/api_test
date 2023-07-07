from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre + self.apellido