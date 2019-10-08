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
        'placeholder':'Password'
        }
    ))	


    