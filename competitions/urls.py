from django.urls import path
from .views import competitions

urlpatterns = [
    path('', competitions, name='competitions'),
]