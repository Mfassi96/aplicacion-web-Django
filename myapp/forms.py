from django import forms
from django.forms import ModelForm
from .models import Task, Project

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Titulo de la tarea",
        # Aquí se añade el widget y la clase form-control
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label="Descripcion de la tarea",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    proyecto = forms.ModelChoiceField(
        label="Proyecto al que pertenece",
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

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
    