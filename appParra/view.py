from tkinter.ttk import Style
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from appParra.models import *


# Create your views here.
def inicio(request):
    return render(request,"C:/Users/Parra/Desktop/proyecto1/ProyecParra/appParra/template/appParra/inicio.html")

def Padre(request):
    Padre= Familiar(nombre = "Carlos", edad = "80", fechaDeNacimiento = "1942-06-30")
    Padre.save()
    return render(request,"C:/Users/Parra/Desktop/proyecto1/ProyecParra/appParra/template/appParra/padre.html")

def mMdre(request):
    Madre= Familiar(nombre = "Nelida", edad = "62", fechaDeNacimiento = "1960-10-10")
    Madre.save()
    return render(request,"C:/Users/Parra/Desktop/proyecto1/ProyecParra/appParra/template/appParra/madre.html")

def Hija(request):
    Hija= Familiar(nombre = "Cecilia", edad = "22", fechaDeNacimiento = "2000-07-23")
    Hija.save()
    return render(request,"C:/Users/Parra/Desktop/proyecto1/ProyecParra/appParra/template/appParra/hija.html")

def comenzar(request):

  
    

    plantillaExterna = open("C:/Users/Parra/Desktop/proyecto1/ProyecParra/ProyecParra/plantillaflia.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    contexto = Context({"Flia1": Padre, "Flia2": Madre, "Flia3": Hija})

    documento = template.render(contexto)
    return HttpResponse(documento)