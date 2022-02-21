from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from user_auth.manager import CustomUserManager
from django.utils import timezone




class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True,null=True,)
    name=models.CharField(max_length=200)
    username=None
    ROLE_CHOICE=(
        ("Admin","Admin"),
        ("Manager","Manager"),
        ("User","User")
    )

    role = models.CharField(choices=ROLE_CHOICE,default='User', max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name',]

    objects = CustomUserManager()

    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.email



