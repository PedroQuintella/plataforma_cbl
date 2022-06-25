from django import forms
from cbl_app.models import Desafio

class SignupForm(forms.Form):
    firstName = forms.CharField(label='Nome')
    lastName = forms.CharField(label='Sobrenome')
    username = forms.CharField(label='Usuário')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class DesafioForm(forms.ModelForm):

    class Meta:
        model = Desafio
        fields = '__all__'
