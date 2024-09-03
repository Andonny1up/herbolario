from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import LoginForm

# Create your views here.

class LoginView(AuthLoginView):
    """
        Vista para autenticar a los usuarios
        formulario con email y password
        redirije al dashboar si se esta ya autenticado.
    """
    template_name = 'dashboard/register/login.html'
    authentication_form = LoginForm

