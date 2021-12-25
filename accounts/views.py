from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from accounts.forms import LoginForm


class Login(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})


class Logout(LogoutView):
    next_page = "login"
