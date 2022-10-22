from html.entities import html5
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def about(request):
    return HttpResponse("About")   


def store(request):
    return HttpResponse("Esto es el store")



