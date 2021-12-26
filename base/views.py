from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, RedirectView

from accounts.models import CustomUser
from base.forms import SchemeForm, ColumnFormset
from base.models import Scheme
from services.tasks import generate_data


class SchemasList(LoginRequiredMixin, ListView):
    template_name = "schemas.html"
    model = Scheme
    context_object_name = "schemas"
    login_url = "login"

    def get_queryset(self):
        """
        Return the list of items for this view.
        """
        user = CustomUser.objects.get(email=self.request.user.email)
        return user.scheme.all()


class CreateSchemeAndColumn(LoginRequiredMixin, CreateView):
    form_class = SchemeForm
    template_name = "new_scheme.html"
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CreateSchemeAndColumn, self).get_context_data(**kwargs)
        context["column_formset"] = ColumnFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        column_formset = ColumnFormset(self.request.POST)
        if form.is_valid() and column_formset.is_valid():
            return self.form_valid(form, column_formset)
        else:
            return self.form_invalid(form, column_formset)

    def form_valid(self, form, column_formset):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        for column in column_formset:
            new_column = column.save(commit=False)
            new_column.scheme = self.object
            try:
                column.save()
            except IntegrityError:
                self.object.delete()
                self.form_invalid(form, column_formset)
        return redirect(
            reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})
        )

    def form_invalid(self, form, column_formset):
        return self.render_to_response(
            self.get_context_data(form=form, column_formset=column_formset)
        )


class DataSets(ListView):
    template_name = "data_sets.html"
    model = Scheme
    context_object_name = "schemas"
    url = "/"


class GenerateData(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return redirect(reverse("datasets", kwargs={"uuid": self.request.user.uuid}))

    def post(self, request, *args, **kwargs):
        user_id = request.user.pk
        quantity = request.POST.get("quantity")

        # Celery task run
        generate_data.delay(user_id, quantity)
        return redirect(
            reverse_lazy("datasets", kwargs={"uuid": self.request.user.uuid})
        )
