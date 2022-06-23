from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from .views import IndexView, AboutView, LoginView, LogoutView, SignupView, RecuperacaoSenhaView, RedefinicaoSenhaView, ConfirmacaoRedefinicaoView, EmailEnviadoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', AboutView.as_view(), name='sobre'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', SignupView.as_view(), name='signup'),
    path('redefinicao-senha/', RedefinicaoSenhaView.as_view(), name='redefinicaoSenha'),
    path('confirmacao-de-redefinicao/', ConfirmacaoRedefinicaoView.as_view(), name='confirmacaoRedefinicao'),
    path('esqueci-senha/', auth_views.PasswordResetView.as_view(template_name="password_recovery.html"), name="reset_password"),
    path('email-recuperacao-enviado/', auth_views.PasswordResetDoneView.as_view(template_name="recovery_email_sent.html"), name="password_reset_done"),
    path('redefinicao/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset.html"), name="password_reset_confirm"),
    path('senha-redefinida/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_confirmation.html"), name="password_reset_complete"),
]