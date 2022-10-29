from urllib import request
from django import forms



class CrearNuevaTareas(forms.Form):
    titulo = forms.CharField(label="Titulo Tareas", max_length=200)
    descripcion = forms.CharField(label="Descipcion de Tarea",widget=forms.Textarea)
