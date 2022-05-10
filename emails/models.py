from django.db import models
from datetime import datetime

from django.db.models import ForeignKey, PROTECT


class Persons(models.Model):
    Cedula = models.IntegerField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Tel = models.IntegerField(max_length=11)
    Edad = models.IntegerField(max_length=11)
    Ciudad = models.CharField(max_length=100)
    purchaseDate = models.DateField(default=datetime.now)
    producto = models.CharField(max_length=100)



