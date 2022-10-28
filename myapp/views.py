from email import message
from html.entities import html5
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto, Tareas
from django.shortcuts import get_object_or_404
# Create your views here.

def hello(request):    
    tittle = "Hola! Bienvenido a mi web con Django" 
    return render(request, 'index.html', {
        "tittle": tittle
    })
    
               

def about(request):
    return render(request,"about.html")   


def store(request):
    return render (request, "store.html")

def projects(request):
    #proyecto = list(Proyecto.objects.values())
    return render(request, "project.html")

def tasks(request):
    #tareas = get_object_or_404(Tareas, id = id)
    return render(request, "tasks.html")



