from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser
from services.generators import generate_uuid, generate_file_path


class Scheme(models.Model):
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="scheme",
    )
    title = models.CharField(
        _("Title"),
        max_length=50,
        blank=False,
        null=False,
    )
    file = models.FileField(
        _("File"), upload_to=generate_file_path, blank=True, null=True
    )
    uuid = models.UUIDField(default=generate_uuid, db_index=True, unique=True)

    created_date = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_("Modified"), auto_now=True)

    is_waiting = models.BooleanField(_("Waiting"), default=True)
    is_processing = models.BooleanField(_("Processing"), default=False)
    is_ready = models.BooleanField(_("Ready"), default=False)
    is_failed = models.BooleanField(_("Failed"), default=False)

    objects = models.Manager()

    class Meta:
        verbose_name = _("Scheme")
        verbose_name_plural = _("Schemas")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("scheme", kwargs={"uuid": self.uuid})


class Column(models.Model):
    class Kind(models.TextChoices):
        FNM = "Full Name", "Full Name"
        JOB = "Job", "Job"
        EML = "Email", "Email"
        DMN = "Domain name", "Domain name"
        PHN = "Phone number", "Phone number"
        CMP = "Company name", "Company name"
        TXT = "Text", "Text"
        INT = "Integer", "Integer"
        ADR = "Address", "Address"
        DAT = "Date", "Date"

    scheme = models.ForeignKey(
        verbose_name=_("Scheme"),
        to=Scheme,
        on_delete=models.CASCADE,
        related_name="column",
        blank=True,
        null=True,
    )
    name = models.CharField(
        _("Column name"),
        max_length=50,
        blank=False,
        null=False,
    )
    kind = models.CharField(
        _("Type"), max_length=20, blank=False, null=False, choices=Kind.choices
    )
    order = models.SmallIntegerField(_("Order"), blank=False, null=False)

    objects = models.Manager()

    class Meta:
        verbose_name = _("Column")
        verbose_name_plural = _("Columns")

    def __str__(self):
        return self.name
