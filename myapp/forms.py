from django import forms
from django.forms import ModelForm
from .models import Task

class CreateNewTask(forms.Form):
    title=forms.CharField(label="Titulo de la tarea")
    description=forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)


class editar_tarea(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Titulo de la tarea',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descripcion de la tarea',
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'Titulo de la tarea',
            'description': 'Descripcion de la tarea',
        }



# formulario para crear un nuevo proyecto
class CreateNewProject(forms.Form):
    name=forms.CharField(label="Titulo del proyecto",widget=forms.TextInput(attrs={
        'placeholder':'Nombre del proyecto',
        'class':'form-control'
        }))
    