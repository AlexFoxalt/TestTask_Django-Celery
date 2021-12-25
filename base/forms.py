from django import forms
from django.forms import inlineformset_factory

from base.models import Scheme, Column


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ("title", "separator", "character")


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("name", "kind", "int_start", "int_end", "txt_sentences_quantity", "order")
        widgets = {
            "kind": forms.Select(choices=Column.Kind.choices, attrs={'class': 'kind-choice-form'}),
        }


ColumnFormset = inlineformset_factory(Scheme, Column, form=ColumnForm, extra=1)
