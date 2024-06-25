from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=250)
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' Адрес пользователя:  {self.full_name} '