



from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    pais_choices = (
        ('mexico', 'mexico'),
        ('china', 'china'),
        ('usa', 'usa'),
        ('salvador', 'salvador'),
    )
    email = models.EmailField('Email Address', max_length=254, unique=True)
    username = models.CharField('usuario', max_length=50, unique=True)
    pais = models.CharField('pais', max_length=50, choices=pais_choices)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    objects = UserManager()

   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
