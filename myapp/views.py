from email import message
from html.entities import html5
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Tareas
from django.shortcuts import get_object_or_404
# Create your views here.

def hello(request, username):     
    return HttpResponse(f"Hola {username}")
    
               

def about(request):
    return HttpResponse("About")   


def store(request):
    return HttpResponse("Esto es el store")

def projects(request):
    proyecto = list(Proyecto.objects.values())
    return JsonResponse(proyecto, safe=False)

def tasks(request, id):
    #tareas = Tareas.objects.get(id=id)
    tareas =get_object_or_404(Tareas, id = id)
    return HttpResponse(f"Tarea: {tareas.titulo}")



