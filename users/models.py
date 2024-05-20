import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField(verbose_name='Patronymic', max_length=150, blank=True)
    sex = models.CharField(verbose_name='Sex', max_length=20, blank=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True, default=datetime.datetime(2005, 10, 12))
    phone_number = models.CharField(verbose_name='Phone number', max_length=20, blank=True)

class TaxiDriversCoordinates(models.Model):
    taxi_driver_id = models.CharField(verbose_name='ID таксиста', max_length=250)
    taxi_driver_status = models.CharField(verbose_name='Статус таксиста', max_length=250)
    taxi_driver_coordinates = models.TextField(verbose_name='Координати таксиста')

    def __str__(self):
        return 'Координати таксистів'

    class Meta:
        verbose_name = 'Координати таксиста'
        verbose_name_plural = 'Координати таксистів'