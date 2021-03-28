from django.contrib.auth.views import LoginView, LogoutView
from authentication.forms import AuthenticationCustomForm


class LoginCustomView(LoginView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationCustomForm
    redirect_authenticated_user = False


class LogoutCustomView(LogoutView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationCustomForm
