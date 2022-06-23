# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View
from cbl_app.forms import LoginForm, SignupForm


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class SignupView(View):
    def get(self, request):
        data = {'form': SignupForm()}
        return render(request, 'signup.html', data)

    def post(self, request):
        form = SignupForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if username and password1 and password2 \
                    and password1 == password2:

                user = User.objects.create_user(
                    username=username,
                    password=password1
                )

                if user:
                    return HttpResponseRedirect(reverse('login'))

        data = {
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, 'signup.html', data)

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        data = {'form': LoginForm()}
        return render(request, 'login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        data = {
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, 'login.html', data)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class RecuperacaoSenhaView(LoginRequiredMixin, TemplateView):
    template_name = 'password_recovery.html'

class RedefinicaoSenhaView(LoginRequiredMixin, TemplateView):
    template_name = 'password_reset.html'

class ConfirmacaoRedefinicaoView(LoginRequiredMixin, TemplateView):
    template_name = 'password_reset_confirmation.html'

class EmailEnviadoView(LoginRequiredMixin, TemplateView):
    template_name = 'recovery_email_sent.html'

