"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (user_registration,
                         user_change_information,
                         user_delete,
                         user_login,
                         user_logaut
                         )
from orders.views import (active_orders_add,
                          completed_orders_add,
                          active_orders_change_information,
                          completed_orders_change_information,
                          active_orders_delete,
                          completed_orders_delete,
                          active_orders_view,
                          completed_orders_view
                          )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('registration/', user_registration),
    path('user_change_information/', user_change_information),
    path('user_delete/', user_delete),
    path('login/', user_login),
    path('logaut/', user_logaut),

    path('active_orders_add/', active_orders_add),
    path('completed_orders_add/', completed_orders_add),
    path('active_orders_change_information/', active_orders_change_information),
    path('completed_orders_change_information/', completed_orders_change_information),
    path('active_orders_delete/', active_orders_delete),
    path('completed_orders_delete/', completed_orders_delete),
    path('active_orders_view/', active_orders_view),
    path('completed_orders_view/', completed_orders_view),
]
