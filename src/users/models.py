from typing import Tuple

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from utils.abstract_models import ReprMixin
from . import UserConst
from .manager import UserManager


class User(AbstractBaseUser,
           PermissionsMixin,
           ReprMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = UserConst.EMAIL
    USERNAME_FIELD = UserConst.EMAIL
    REQUIRED_FIELDS = [UserConst.F_NAME, UserConst.L_NAME, UserConst.PASS]

    class Meta:
        verbose_name: str = _('user')
        verbose_name_plural: str = _('users')
        ordering: Tuple[str] = (UserConst.EMAIL,)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def fullname(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return self.fullname
