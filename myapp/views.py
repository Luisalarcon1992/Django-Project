from email import message
from html.entities import html5
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto, Tareas
from django.shortcuts import get_object_or_404
from .forms import CrearNuevaTareas
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
    proyectos = Proyecto.objects.all()
    return render(request, "project.html", {
        "proyectos" : proyectos
    })

def tasks(request):
    #tareas = get_object_or_404(Tareas, id = id)
    tareas = Tareas.objects.all()
    return render(request, "tasks.html", {
        "tareas" : tareas
    })

def creat_task(request):
    if request.method == "GET":
         return render(request, "create_tasks.html", {
        "form" : CrearNuevaTareas()
    })        
    else:
        Tareas.objects.create(titulo=request.POST["titulo"], descipcion = request.method.POST["descripcion"], Proyecto_id = 2)
        return redirect("tasks/")




   