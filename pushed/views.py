from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from .forms import LoginForm
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from .models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def profile(request):
    if request.method == 'POST':
        if request.FILES['myfile']:    
            myfile = request.FILES['myfile']   
            request.user.image = myfile
            request.user.save()    
        # form = PasswordChangeForm(request.user, request.POST)  
        # if form.is_valid():
        #     request.user.set_password(request.POST['new_pass']) 
        #     request.user.save()   
        #     messages.success(request, 'Your password was successfully updated!')
        #     update_session_auth_hash(request, user)   
        # else:
        #     messages.error(request, 'Please correct the error below.')                    
                          
    # Si estamos identificados devolvemos el index
    if request.user.is_authenticated:
        return render(request, "profile.html")
    # En otro caso redireccionamos al login
    return redirect('/login') 
    
def hack(request):
    return render(request, "profile.html")
    
def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })          

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos al index
                return redirect('index')		            
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})    

