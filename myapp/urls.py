from django.urls import path
from . import views



urlpatterns=[
        path('',views.index,name="index"),
        path('about/',views.about,name="about"),
        path('hello/<str:username>',views.hello,name="hello"),
        path('projects/',views.projects,name="projects"),
        path('tasks/',views.tasks,name="tasks"),
        path('createtask/',views.createtask,name="createtask"),
        path('create_project/',views.create_project,name="createproject"),
        path('project_detail/<int:id>',views.project_detail,name="project_detail"),
]