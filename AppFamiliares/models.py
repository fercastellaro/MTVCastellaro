from django.db import models

class Padre(models.Model):

    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    fechaDeNacimiento = models.DateField()


class Madre(models.Model):

    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    fechaDeNacimiento = models.DateField()


class Hermanos(models.Model):

    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    fechaDeNacimiento = models.DateField()
        