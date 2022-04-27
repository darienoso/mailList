from django.db import models
from datetime import datetime


class Persons(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    tel = models.IntegerField(max_length=11)
    age = models.IntegerField(max_length=11)
    city = models.CharField(max_length=100)


class products(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    purchaseDate = models.DateField(default=datetime.now)


class sells(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    productId = models.IntegerField(max_length=11)
    personId = models.IntegerField(max_length=11)
    sellCode = models.IntegerField(max_length=11)
