
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('store/', views.store),
    path('tasks/', views.tasks),
    path('project/', views.projects),
    path('create_tasks/', views.creat_task)
    ]