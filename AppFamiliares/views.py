from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliares.models import Padre, Madre, Hermanos
from django.template import loader, Template, Context


def padre(self):

    diccionario = {'nombre': "Luis", 'apellido': "Castellaro", 'edad': 57, 'fechaDeNacimiento': "1964-8-21"}
    
    plantilla = loader.get_template('padre.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def madre(self):

    diccionario = {'nombre': 'Ana Elisa', 'apellido': 'Almiron', 'edad': 56, 'fechaDeNacimiento': '1965-12-30'}

    plantilla = loader.get_template('madre.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
    

def hermano(self):

    diccionario = {'nombre': 'Hernan', 'apellido': 'Castellaro', 'edad': 26, 'fechaDeNacimiento': '1996-5-23'}
    
    plantilla = loader.get_template('hermano.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def hermanoMasChico(self):

    diccionario = {'nombre': 'Matias', 'apellido': 'Castellaro', 'edad': 24, 'fechaDeNacimiento': '1996-6-22'}
    
    plantilla = loader.get_template('hermano.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)