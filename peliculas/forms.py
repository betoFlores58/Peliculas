from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto

#DECLARACION DE CLASES PARA CREAR USUARIO PERSONALIZADO, FORM PARA CONTACTO Y RESET PASSWORD
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre","correo","tipo","mensaje","avisos"]
        fields = '__all__'
        
class ResetPasswordForm(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un email',
        'class': 'form-control',
        'autocomplete': 'off'
    }))