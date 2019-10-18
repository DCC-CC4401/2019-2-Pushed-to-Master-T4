from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import RegisterForm

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    model = User
    ordering = ()


admin.site.register(User,CustomUserAdmin)