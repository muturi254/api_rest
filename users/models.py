from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from users.managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ()

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email