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
                        messages.success(request, 'Your password was updated successfully!', extra_tags='alert')
                        update_session_auth_hash(request, user)      
                    else:
                        messages.warning(request, 'Please correct the error below.')


        else:
            pass_form = PassForm()
            change_photo = ChangePhoto()
                
        return render(request, "profile.html", {'change_pass': pass_form, 'change_photo': change_photo })                                      
        
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

