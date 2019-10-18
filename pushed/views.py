from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from .forms import *
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from .models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def profile(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = PassForm(request.POST)
            change_photo = ChangePhoto(request.POST, request.FILES)
            if change_photo.is_valid : 
                filepath = request.FILES.get('photo', False) 
                if filepath:
                    myfile = request.FILES['photo'] 
                    request.user.image = myfile
                    request.user.save()  

            if pass_form.is_valid:    
                old_password = request.POST.get("old_password")
                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")                                                       
                if old_password and confirm_password and confirm_password == new_password:
                    if request.user.check_password(old_password):                    
                        request.user.set_password(request.POST['new_password']) 
                        request.user.save()   
                        messages.success(request, 'Se ha actualizado tu contraseña.', extra_tags='alert')
                        update_session_auth_hash(request, request.user)      
                    else:
                        messages.warning(request, 'Debes ingresar tu contraseña actual.')                    
        else:
            pass_form = PassForm()
            change_photo = ChangePhoto()
        
                
        return render(request, "profile.html", {'change_pass': pass_form, 'change_photo': change_photo })
        
    # En otro caso redireccionamos al login
    return redirect('/login') 
 
def seguridad(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = PassForm(request.POST)
            change_photo = ChangePhoto(request.POST, request.FILES)
            if change_photo.is_valid : 
                filepath = request.FILES.get('photo', False) 
                if filepath:
                    myfile = request.FILES['photo'] 
                    request.user.image = myfile
                    request.user.save()  

            if pass_form.is_valid:    
                old_password = request.POST.get("old_password")
                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")                                                       
                if old_password and confirm_password and confirm_password == new_password:
                    if request.user.check_password(old_password):                    
                        request.user.set_password(request.POST['new_password']) 
                        request.user.save()   
                        messages.success(request, 'Se ha actualizado tu contraseña.', extra_tags='alert')
                        update_session_auth_hash(request, request.user)      
                    else:
                        messages.warning(request, 'Debes ingresar tu contraseña actual.')                    
        else:
            pass_form = PassForm()
            change_photo = ChangePhoto()
        
                
        return render(request, "seguridad.html", {'change_pass': pass_form, 'change_photo': change_photo })
        
    # En otro caso redireccionamos al login
    return redirect('/login') 

def actividades(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        return render(request, "actividades.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def amigos(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        return render(request, "amigos.html")
    # En otro caso redireccionamos al login
    return redirect('/login')    

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')

def index(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        return render(request, "index.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def login(request):
    if request.method == 'POST' and 'login' in request.POST:
        form = LoginForm(request.POST)
        registro = RegisterForm()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos al index
                return redirect('index')

    elif request.method == 'POST' and 'registrar' in request.POST: 
        registro = RegisterForm(request.POST) 
        form = LoginForm()               
        if registro.is_valid():
            registro.save()
            first_name = registro.cleaned_data['first_name']
            last_name = registro.cleaned_data['last_name']
            email = registro.cleaned_data['email']
            password =  registro.cleaned_data['password1']
            password2 =  registro.cleaned_data['password2']
            user = authenticate(email=email, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos al index
                return redirect('index')                 		            
    else:
        form = LoginForm()
        registro = RegisterForm()
    return render(request, "login.html", {'form': form,'registro': registro})    

