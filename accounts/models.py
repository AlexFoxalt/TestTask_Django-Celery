from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager
from services.generators import generate_uuid


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Default model for describing user on this project"""

    email = models.EmailField(
        _("Email"),
        unique=True,
        help_text=_("Required field! Ex: my_email@example.com"),
        error_messages={
            "unique": _(
                "User with such email already exists. Choose another email, or login via one"
            )
        },
    )
    uuid = models.UUIDField(default=generate_uuid, db_index=True, unique=True)

    date_joined = models.DateTimeField(_("Date joined"), auto_now_add=True)
    is_staff = models.BooleanField(
        _("Is staff"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Is active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.email
