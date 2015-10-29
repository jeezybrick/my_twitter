from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.core import validators
from django.utils import timezone
from core.models import TimeStampedModel
from my_auth.managers import CustomUserManager


# Extend User model
class MyUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    username = models.CharField(_('username'), max_length=30, unique=True, blank=False,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    full_name = models.CharField(_('Full name'), max_length=50, blank=False)
    email = models.EmailField(_('Email'), blank=False, unique=True, db_index=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', ]
    objects = UserManager()

    def __unicode__(self):
        return self.email

    class Meta(object):
        unique_together = ('email',)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.full_name.strip()


class OAuthUser(AbstractBaseUser):

    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True
