from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.profile, name='profile'),
    path('login', views.login , name='login'),
    path('registrar', views.registrar , name='registrar'),      
    path('logout', views.logout),
    path('seguridad', views.seguridad,name='seguridad'),
    path('amigos', views.amigos,name='amigos'),
    path('actividades', views.actividades,name='actividades'),
    path(r'profile/<int:id>/<str:nombre>', views.friendprofile, name="amigo"),
]