from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField()
    avatar = models.ImageField()
    birth_date = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
