from django.urls import path
from . import views



urlpatterns=[
        path('',views.index,name="index"),
        path('about/',views.about,name="about"),
        path('hello/<str:username>',views.hello,name="hello"),
        path('projects/',views.projects,name="projects"),
        # RUTAS PARA LAS TAREAS ------------------------------------
        path('tasks/',views.tasks,name="tasks"),
        path('tasks_delete_alert/<int:id>',views.task_delete_alert,name="task_delete_alert"),
        path('tasks_delete/<int:id>',views.tasks_delete,name="tasks_delete"),
        path('tasks/edit_tasks/<int:id>',views.edit_tasks,name="edit_task"),
        path('tasks/update_task/<int:id>',views.update_tasks,name="update_task"),
         # ------------------
        path('createtask/',views.createtask,name="createtask"),
        path('create_project/',views.create_project,name="createproject"),
        path('project_detail/<int:id>',views.project_detail,name="project_detail"),
]