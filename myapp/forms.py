from django import forms

class CreateNewTask(forms.Form):
    title=forms.CharField(label="Titulo de la tarea")
    description=forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)

# formulario para crear un nuevo proyecto
class CreateNewProject(forms.Form):
    name=forms.CharField(label="Titulo del proyecto",widget=forms.TextInput(attrs={
        'placeholder':'Nombre del proyecto',
        'class':'form-control'
        }))
    