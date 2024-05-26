from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('accounts/profile/', profile_view, name="profile"),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/registration/', views.signup, name='registration'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
