from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.profile, name='profile'),
    path('login', views.login , name='login'),
    path('logout', views.logout),
]