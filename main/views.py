from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from news.models import Article
from competitions.models import Competitions
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
def index(request):
    articles = Article.objects.all()
    #    competitions = Competitions.objects.filter(date__gte=now()).order_by('date') #Выводит текущие (актульные соревнования), отключено для тестов!
    competitions = Competitions.objects.all()
    context = {'articles': articles, 'competitions': competitions}
    if request.user.is_authenticated:
        return render(request, 'main/index.html', {'user': request.user , 'is_authenticated':request.user.is_authenticated } | context)
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/accounts/profile') 
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def profile_view(request):
    username = request.user.username
    return render(request, "main/profile.html", {'username': username})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'auth/registration.html', {'form': form})
