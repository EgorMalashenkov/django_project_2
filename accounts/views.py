from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import SignUpForm


class SignupView(CreateView):
    success_url = "login"
    form_class = SignUpForm
    template_name = 'accounts/register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/login.html"