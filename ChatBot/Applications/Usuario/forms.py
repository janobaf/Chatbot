from django import forms
from django.contrib.auth import authenticate
from .models import usuario


class FormularioRegistroForm(forms.ModelForm):

    password1=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    class Meta:
        model = usuario
        fields = (
                    'username',
                    'nombre',
                    'imagen',
                    'roles',
        
                )

    def clean_password(self):
        password=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        espacio= False
        minuscula = False
        mayuscula = False
        numeros = False
        digitos=len(password)
        for e in digitos:
            if e.isspace():
                espacio=True
            elif e.islower():
                minuscula=True
            elif e.isupper():
                mayuscula=True
            elif e.isdigit():
                numeros=True
        if digitos== password2:
            self.add_error('password2','Las contraseñas no son las mismas')

        if minuscula==False and mayuscula==False and numeros==False and espacio==False and digitos>=6:
             self.add_error('password1','Las contraseñas deven de tener almenos 1 minuscula 1 mayuscula 1 numero y deve de ser de mas de 6 digitos')



        

class LoginForm(forms.Form):

    username=forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username'
            }
        )
    )

    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data=super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']


        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        return self.cleaned_data
        
