from django.shortcuts import *
from app1.models import *

# Create your views here.
def insertView(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        dueTime = request.POST['dueTime']
        due_date = request.POST['due_date']
        Task.objects.create(
            title=title,
            description=description,
            dueTime=dueTime,
            due_date=due_date
        )
        return redirect('indexView')
    else:
        return render(request, 'insert.html')  # <-- Needed for GET


def index(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'index.html',{'tasks':tasks})

def toggle_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()

    return redirect('indexView')

def del_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect('indexView')

