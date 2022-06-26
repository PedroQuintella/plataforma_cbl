# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Desafio, User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView
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
            firstName = form.cleaned_data.get('firstName')
            lastName = form.cleaned_data.get('lastName')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if firstName and lastName and username and email and password1 and password2 \
                    and password1 == password2:

                user = User.objects.create_user(
                    first_name=firstName,
                    last_name=lastName,
                    username=username,
                    email=email,
                    password=password1
                )

                if user:
                    userLogin = authenticate(request, username=username, password=password1)
                    login(request, userLogin)
                    return HttpResponseRedirect(reverse('contaUsuario'))

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


class ContaUsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super(ContaUsuarioView, self).get_context_data(**kwargs)
        context['usuario'] = User.objects.filter(username=self.request.user.username)
        return context


class EdicaoContaView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_account.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy("contaUsuario")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(User, username=self.request.user.username)
        return self.object

    def get_context_data(self, **kwargs):
        context = super(EdicaoContaView, self).get_context_data(**kwargs)
        context['usuario'] = User.objects.filter(username=self.request.user.username)
        return context


class NovoDesafioView(LoginRequiredMixin, CreateView):
    template_name = 'new_challenge.html'
    model = Desafio
    fields = '__all__'
    success_url = reverse_lazy('meusDesafios')

    def get_context_data(self, **kwargs):
        context = super(NovoDesafioView, self).get_context_data(**kwargs)
        context['desafio'] = Desafio.objects.filter(usuario=self.request.user)
        return context


class MeusDesafiosView(LoginRequiredMixin, ListView):
    template_name = 'my_challenges.html'
    model = Desafio
    paginate_by = 6
    ordering = ['dataCriacao']

    def get_context_data(self, **kwargs):
        context = super(MeusDesafiosView, self).get_context_data(**kwargs)
        context['desafio'] = Desafio.objects.filter(usuario=self.request.user)
        return context

    def get_queryset(self):
        return Desafio.objects.order_by('dataCriacao').all()


class DesafioView(LoginRequiredMixin, UpdateView):
    template_name = 'challenge.html'
    model = Desafio
    fields = ['titulo', 'grandeIdeia', 'questaoEssencial', 'desafios', 'documentosEnvolver',
                    'questoesNorteadoras', 'recursos', 'atividades', 'sintese', 'documentosInvestigar',
                    'conceitosSolucao', 'implementacaoSolucao', 'avaliacao', 'documentosAgir', 'usuario']
    success_url = reverse_lazy("meusDesafios")

    def get_object(self, queryset=None, **kwargs):
        id = self.kwargs['id']
        self.object = get_object_or_404(Desafio, id=id)
        return self.object

    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        context = super(EdicaoContaView, self).get_context_data(**kwargs)
        context['desafio'] = Desafio.objects.filter(id=id)
        return context

    def get_context_data(self, **kwargs):
        context = super(DesafioView, self).get_context_data(**kwargs)
        context['desafio'] = Desafio.objects.filter(usuario=self.request.user)
        id = self.kwargs['id']
        context['desafio'] = Desafio.objects.filter(id=id).first
        return context


class RecuperacaoSenhaView(LoginRequiredMixin, TemplateView):
    template_name = 'password_recovery.html'


class RedefinicaoSenhaView(LoginRequiredMixin, TemplateView):
    template_name = 'password_reset.html'


class ConfirmacaoRedefinicaoView(LoginRequiredMixin, TemplateView):
    template_name = 'password_reset_confirmation.html'


class EmailEnviadoView(LoginRequiredMixin, TemplateView):
    template_name = 'recovery_email_sent.html'