from django.contrib import admin
from .models import Project,Task

# Register your models here.
# registra los modelos en la pagina del administrador
admin.site.register(Project)
admin.site.register(Task)

