from django.db import models


class ActiveOrders(models.Model):
    opening_time = models.DateTimeField()
    starting_address = models.TextField()
    final_address = models.TextField()
