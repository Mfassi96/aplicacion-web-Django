from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateNewTask
from .forms import CreateNewProject

# importar los modelos
from .models import Project,Task

# Create your views here.

def index(request):
    return render(request,'index.html')

def hello(request, username):
    return HttpResponse(f"Hello {username}")

# def about(request):
#     return render(request,'About.html')

def projects(request):
    #projects=list(Project.objects.values())
    projects=Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects_list':projects
    })

def tasks(request):
    tasks=Task.objects.all()
    return render(request,"tasks/task.html",{
        "task_list":tasks
    })

def about(request):
    return render(request,'about.html')

def createtask(request):
    #title=request.GET['title']
    #description=request.GET['description']
    if (request.method =='GET'):
        #mostraar interfaz
        return render(request,'tasks/create_task.html',{
            'form':CreateNewTask()
        })
    else:
        project_instance = Project.objects.get(id=2)
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'],
        project=project_instance)
        return redirect('/tasks/')
       
def create_project(request):
    if (request.method=='GET'):
        return render(request,'projects/create_project.html',{
            'form':CreateNewProject()
    })
    else:
        #project_instance=projects.objects.get(id=2)
        #print(request.POST)
        Project.objects.create(name=request.POST['name'])
        return render(request,'projects/create_project.html',{
            'form':CreateNewProject()
        })

def project_detail(request,id):
    # project=Project.objects.get(id=id)
    project=get_object_or_404(Project, id=id)
    tareas=Task.objects.filter(project=project)
    return render(request,'projects/project_detail.html',{
        'id':id,
        'project':project,
        'tasks':tareas})
    
def task_delete_alert(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/task_delete_alert.html', {
        'task': task
    })

def tasks_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('/tasks/')