import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField(verbose_name='Patronymic', max_length=150, blank=True)
    sex = models.CharField(verbose_name='Sex', max_length=20, blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True, default=datetime.datetime(2005, 10, 12))
    phone_number = models.CharField(verbose_name='Phone number', max_length=20, blank=True)
