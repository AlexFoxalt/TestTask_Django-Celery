from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser
from services.generators import generate_uuid, generate_file_path


class Scheme(models.Model):
    class Separator(models.TextChoices):
        PNT = ".", "Point (.)"
        COM = ",", "Coma (,)"

    class Character(models.TextChoices):
        DQT = "\"", "Double-quote (\")"
        SQT = "'", "Singe-quote (')"

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
    separator = models.CharField(
        _("Column separator"),
        max_length=5,
        blank=False,
        null=False,
        choices=Separator.choices,
        default=Separator.PNT
    )
    character = models.CharField(
        _("String character"),
        max_length=5,
        blank=False,
        null=False,
        choices=Character.choices,
        default=Character.DQT
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

    def set_processing(self):
        self.is_waiting = False
        self.is_processing = True

    def set_ready(self):
        self.is_processing = False
        self.is_ready = True

    def set_failed(self):
        self.is_processing = False
        self.failed = True


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
        _("Type"), max_length=20, blank=False, null=False, choices=Kind.choices, default=Kind.FNM
    )
    order = models.SmallIntegerField(_("Order"), blank=False, null=False)

    int_start = models.IntegerField(
        _("From"),
        blank=False,
        null=False,
        default=0
    )
    int_end = models.IntegerField(
        _("To"),
        blank=False,
        null=False,
        default=1_000_000
    )
    txt_sentences_quantity = models.IntegerField(
        _("Sentences"),
        blank=False,
        null=False,
        default=3
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _("Column")
        verbose_name_plural = _("Columns")

    def __str__(self):
        return self.name
