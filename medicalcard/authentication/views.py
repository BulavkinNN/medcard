from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from authentication.forms import AuthenticationCustomForm


class LoginCustomView(LoginView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationCustomForm
    redirect_authenticated_user = False


class LogoutCustomView(LogoutView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationCustomForm

class PasswordChangeCustomView(PasswordChangeView):
    template_name = 'authentication/password_change_form.html'

class PasswordChangeDoneCustomView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'

class PasswordResetCustomView(PasswordResetView):
    template_name = 'authentication/password_reset_form.html'
    email_template_name = 'authentication/password_reset_email.html'
    success_url = reverse_lazy('authentication:password_reset_done')

class PasswordResetDoneCustomView(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class PasswordResetConfirmCustomView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PasswordResetCompleteCustomView(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
