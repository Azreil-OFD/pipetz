from django.shortcuts import render
from django.utils.timezone import now
from .models import Competitions


def competitions(request):
#    competitions = Competitions.objects.filter(date__gte=now()).order_by('date') #Выводит текущие (актульные соревнования), отключено для тестов!
    competitions = Competitions.objects.all()
    return render(request, 'competitions/competitions.html', {'competitions': competitions})