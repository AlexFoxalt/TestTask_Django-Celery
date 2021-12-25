from django.urls import path

from base.views import (
    SchemasList,
    CreateSchemeAndColumn, DataSets, GenerateData,
)

urlpatterns = [
    path("schemas/<uuid:uuid>", SchemasList.as_view(), name="schemas"),
    path("scheme/new", CreateSchemeAndColumn.as_view(), name="new_scheme"),
    path("datasets/<uuid:uuid>", DataSets.as_view(), name="datasets"),
    path("generate-data/", GenerateData.as_view(), name="generate-data")
]
