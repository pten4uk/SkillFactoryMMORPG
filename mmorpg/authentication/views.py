from django.contrib.auth import get_user_model
from django.shortcuts import render

from allauth.account.views import LoginView, SignupView

from .forms import CustomLoginForm, CustomSignupForm

User = get_user_model()


class CustomLogin(LoginView):
    form_class = CustomLoginForm

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class CustomSignup(SignupView):
    form_class = CustomSignupForm