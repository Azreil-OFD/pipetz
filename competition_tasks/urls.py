from django.urls import path
from .views import competitions_tasks

urlpatterns = [
    path('', competitions_tasks, name='competitions_tasks'),
]