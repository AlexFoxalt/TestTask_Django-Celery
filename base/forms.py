from django import forms
from django.forms import inlineformset_factory

from base.models import Scheme, Column


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ("title",)


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("name", "kind", "order")


ColumnFormset = inlineformset_factory(Scheme, Column, form=ColumnForm, extra=1)
