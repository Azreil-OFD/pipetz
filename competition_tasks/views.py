from django.shortcuts import render
from .models import Competition_tasks

def competition_tasks(request):
    tasks = Competition_tasks.objects.all()
    return render(request, 'competition_tasks/competition_tasks.html', {'tasks': tasks})

