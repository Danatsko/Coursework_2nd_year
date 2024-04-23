from django.db import models


class ActiveOrders(models.Model):
    opening_time = models.DateTimeField(verbose_name='Час відкриття замовлення')
    starting_address = models.TextField(verbose_name='Початкова адреса')
    final_address = models.TextField(verbose_name='Кінцева адреса')

    def __str__(self):
        return 'Активні замовлення'

    class Meta:
        verbose_name = 'Активне замовлення'
        verbose_name_plural = 'Активні замовлення'


class CompletedOrders(models.Model):
    taxi_driver = models.CharField(verbose_name='Таксист', max_length=150)
    opening_time = models.DateTimeField(verbose_name='Час відкриття замовлення')
    closing_time = models.DateTimeField(verbose_name='Час закриття замовлення')
    starting_address = models.TextField(verbose_name='Початкова адреса')
    final_address = models.TextField(verbose_name='Кінцева адреса')
    price = models.FloatField(verbose_name='Ціна')

    def __str__(self):
        return 'Завершені замовлення'

    class Meta:
        verbose_name = 'Завершене замовлення'
        verbose_name_plural = 'Завершені замовлення'