from django.urls import path
from django.views.generic import RedirectView

from accounts.views import Login, Logout

urlpatterns = [
    path("", RedirectView.as_view(url="login"), name="index"),
    path("login/", Login.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
