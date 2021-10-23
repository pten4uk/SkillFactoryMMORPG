from allauth.account.forms import LoginForm, PasswordField
from allauth.utils import get_username_max_length
from django import forms
from django.contrib.auth import get_user_model
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomLoginForm(LoginForm):
    password = CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control rounded-4"
            }
        )
    )
    remember = forms.BooleanField(
        label=_("Remember Me"),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        login_widget = forms.TextInput(
            attrs={
                "placeholder": _("Username"),
                "autocomplete": "username",
                "class": "form-control rounded-4"
            },
        )
        login_field = forms.CharField(
            label=_("Username"),
            widget=login_widget,
            max_length=get_username_max_length(),
        )

        self.fields["login"] = login_field

    def clean_login(self):
        login = self.cleaned_data['login']
        if not User.objects.filter(username=login).first():
            raise forms.ValidationError('Такого имени пользователя не существует')
        return login

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

