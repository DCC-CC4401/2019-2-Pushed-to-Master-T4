from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import RegisterForm

admin.site.register(User)