from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def index(request):
    return render_to_response('index.html')

def profile(request):
    return render_to_response('profile.html')   

def login(request):
    return render_to_response('login.html')   
