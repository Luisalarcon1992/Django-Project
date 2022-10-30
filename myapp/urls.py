
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="index"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('tasks/', views.tasks, name="tasks"),
    path('project/', views.projects, name="project"),
    path('create_tasks/', views.creat_task, name="create_tasks"),
    path('create_project/', views.creat_project, name="create_project")
    ]