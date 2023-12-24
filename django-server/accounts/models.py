from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    organization = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=15, null=True)
    phoneNumber = PhoneNumberField(null=True)