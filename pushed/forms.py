from django import forms
from django.contrib.auth.forms import UserCreationForm
from pushed.models import User

class LoginForm(forms.Form):
    email = forms.CharField(label='',widget=forms.EmailInput(
        attrs={
        'class':'ggg',
        'placeholder':'ejemplo@dominio.com'
        }   
    ))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={
        'class':'ggg',
        'placeholder':'********'
        }
    ))	

class ChangePhoto(forms.Form):
    photo = forms.FileField(label='',required=False,widget=forms.ClearableFileInput(
        attrs={
        'id':'files',
        'onchange':'this.form.submit()',
        }
    )
    )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Nombre'
        }
    ))

    last_name = forms.CharField(max_length=20,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Apellido'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
        'class':'form-control',
        'placeholder':'ejemplo@dominio.com'
        }   
    ))  

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Ingrese contraseña'
        }
    ))   

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Confirma contraseña'
        }
    ))  

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'password1', 'password2',)   

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']        
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

class ChangePhoto(forms.Form):
    photo = forms.FileField(label='',required=False,widget=forms.ClearableFileInput(
        attrs={
        'id':'files',
        'onchange':'this.form.submit()',
        }
    )
    )

class PassForm(forms.Form):
    new_password = forms.CharField(label='Nueva contraseña',widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'id':'newpass',
        'placeholder':'Nueva contraseña'
        }
    ))
    confirm_password = forms.CharField(label='Confirme nueva contraseña',widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'id': 'confirmpass',
        'placeholder':'Confirme nueva contraseña'
        }
    ))  
    old_password = forms.CharField(label='Ingrese contraseña actual:',widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'id': 'oldpass',
        'placeholder':'********'
        }
    ))      



    