from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(
        attrs={
        'class':'ggg',
        'placeholder':'Username'
        }
   )
    )
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



    