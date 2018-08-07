from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
# Create your models here.


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    academic_level = models.CharField(default='', max_length=100, blank=True, null=True, verbose_name="Municipio")
    address = models.CharField(default='', max_length=200, blank=True, null=True, verbose_name="Address")
    city = models.CharField(default='', max_length=50, blank=True, null=True, verbose_name="City")
    country = models.CharField(default='', max_length=80, blank=True, null=True, verbose_name="Country")

    def __str__(self):
        return str(self.user.username) + " " + self.user.email
