from django.urls import path, re_path
from django.views.generic.base import RedirectView

from base.views import (
    SchemasList,
    CreateSchemeAndColumn,
    DataSets,
    GenerateData,
)

favicon_view = RedirectView.as_view(url="/CSVFaker/static/favicon.ico", permanent=True)

urlpatterns = [
    path("schemas/<uuid:uuid>", SchemasList.as_view(), name="schemas"),
    path("scheme/new", CreateSchemeAndColumn.as_view(), name="new_scheme"),
    path("datasets/<uuid:uuid>", DataSets.as_view(), name="datasets"),
    path("generate-data/", GenerateData.as_view(), name="generate-data"),
    re_path(r"^favicon\.ico$", favicon_view),
]
