
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('tasks/<int:id>', views.tasks),
    path('proyects/', views.projects)
    ]