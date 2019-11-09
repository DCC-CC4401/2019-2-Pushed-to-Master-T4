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
from django.http import JsonResponse

def profile(request):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        if request.method == 'POST':
            change_photo = ChangePhoto(request.POST, request.FILES)
            if change_photo.is_valid : 
                filepath = request.FILES.get('photo', False) 
                if filepath:
                    myfile = request.FILES['photo'] 
                    request.user.image = myfile
                    request.user.save()                   
        else:
            change_photo = ChangePhoto()
        
                
        return render(request, "profile.html", {'change_photo': change_photo })
        
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

            # View para el formulario de pass, retorno un json response, que lo catchea el ajax changepass.js
            if pass_form.is_valid:   
                old_password = request.POST.get("old_password")
                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")                                                       
                if old_password and confirm_password and confirm_password == new_password:
                    if request.user.check_password(old_password):                    
                        request.user.set_password(request.POST['new_password']) 
                        request.user.save()   
                        update_session_auth_hash(request, request.user)     
                        return JsonResponse('Se ha modificado tu constraseña.',safe=False)  
                    else:
                        return JsonResponse('La clave actual que has ingresado no es correcta.',safe=False)   
                else: 
                    return JsonResponse('La confirmación de tu contraseña no coincide.',safe=False)                                        
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
        data=User.objects.all()
        return render(request, "amigos.html",{'data': data})
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
    registro = RegisterForm()  
    if request.method == 'POST' and 'login' in request.POST:
        form = LoginForm(request.POST)
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
    else:
        form = LoginForm() 
    return render(request, "login.html", {'form': form, 'registro': registro})    

def registrar(request):
    if request.method == 'POST' and 'registrar' in request.POST: 
        registro = RegisterForm(request.POST, request.FILES)                
        if registro.is_valid():
            instancia = registro.save(commit=False)          
            instancia.save()      
            first_name = registro.cleaned_data['first_name']
            last_name = registro.cleaned_data['last_name']
            email = registro.cleaned_data['email']
            password =  registro.cleaned_data['password1']            
            user = authenticate(email=email, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos al index
                return HttpResponse('')
        else:
            return JsonResponse(registro.errors)   
    else:
        registro = RegisterForm()             
    return render(request, "registro.html", {'registro': registro})              


def friendprofile(request, nombre,id):
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:     
        data=search(User.objects.values(),id)
        img=data.get('image')
        apellido=data.get('last_name')
        correo = data.get('email')
        return render(request, "friend.html",{'name':nombre,'apellido':apellido,'img':img,'email':correo})
        
    # En otro caso redireccionamos al login
    return redirect('/login') 

def search(json_object, name):
    for dict in json_object:
        if dict['id'] == name:
            return dict