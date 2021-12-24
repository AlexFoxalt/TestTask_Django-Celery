from django.urls import path
from django.views.generic import RedirectView

from base.views import (
    Login,
    Logout,
    SchemasList,
    UpdateScheme,
    DeleteScheme,
    DetailedScheme,
    CreateSchemeAndColumn,
)

urlpatterns = [
    path("", RedirectView.as_view(url="login"), name="index"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("schemas/<uuid:uuid>", SchemasList.as_view(), name="schemas"),
    path("scheme/<uuid:uuid>", DetailedScheme.as_view(), name="scheme"),
    path("scheme/new", CreateSchemeAndColumn.as_view(), name="new_scheme"),
    path("scheme/<uuid:uuid>/update", UpdateScheme.as_view(), name="update_scheme"),
    path("scheme/<uuid:uuid>/delete", DeleteScheme.as_view(), name="delete_scheme"),
]
