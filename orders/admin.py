from django.contrib import admin
from .models import ActiveOrders, CompletedOrders


admin.site.register(ActiveOrders)
admin.site.register(CompletedOrders)
