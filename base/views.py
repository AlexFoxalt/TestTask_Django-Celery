from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from accounts.forms import LoginForm
from accounts.models import CustomUser
from base.forms import SchemeForm, ColumnFormset
from base.models import Scheme


class Login(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})


class Logout(LogoutView):
    next_page = "login"


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


class DetailedScheme(DetailView):
    template_name = "scheme.html"
    model = Scheme

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        """
        uuid = self.kwargs.get("uuid")
        return Scheme.objects.get(uuid=uuid)


class UpdateScheme(UpdateView):
    template_name = "scheme_update.html"

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        """
        uuid = self.kwargs.get("uuid")
        return Scheme.objects.get(uuid=uuid)

    def get_success_url(self):
        return reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})


class DeleteScheme(DeleteView):
    template_name = "scheme_confirm_delete.html"

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        """
        uuid = self.kwargs.get("uuid")
        return Scheme.objects.get(uuid=uuid)

    def get_success_url(self):
        return reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})


class CreateSchemeAndColumn(CreateView):
    form_class = SchemeForm
    template_name = "new_scheme.html"

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
            column.save()
        return redirect(
            reverse_lazy("schemas", kwargs={"uuid": self.request.user.uuid})
        )

    def form_invalid(self, form, column_formset):
        return self.render_to_response(
            self.get_context_data(form=form, column_formset=column_formset)
        )
