from django.db import models
from datetime import datetime

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    edad = models.IntegerField()
    fnac = models.DateField(null=True)
