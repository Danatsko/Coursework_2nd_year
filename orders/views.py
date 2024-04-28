import datetime
import json

from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from orders.models import (ActiveOrders,
                           CompletedOrders)


@csrf_protect
def active_orders_add(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')
        operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')

        if admin_group_created:
            admin_group.permissions.add(21)
            admin_group.permissions.add(22)
            admin_group.permissions.add(23)
            admin_group.permissions.add(24)
            admin_group.permissions.add(25)
            admin_group.permissions.add(26)
            admin_group.permissions.add(27)
            admin_group.permissions.add(28)
            admin_group.permissions.add(29)
            admin_group.permissions.add(30)
            admin_group.permissions.add(31)
            admin_group.permissions.add(32)

        if operator_group_created:
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)

        if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='Operator').exists():
            if request.method == 'POST':
                parameters = dict(json.loads(request.body))

                if (('opening time' in parameters) and
                        ('starting address' in parameters) and
                        ('final address' in parameters) and
                        (len(parameters) == 3)
                ):
                    order = ActiveOrders(opening_time=datetime.datetime(*list(map(int, parameters['opening time'].split()))),
                                         starting_address=parameters['starting address'],
                                         final_address=parameters['final address']
                                         )
                    order.save()

                    answer = {'Status': 'Success',
                              'Message': 'Created.'
                              }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Wrong parameters.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Wrong method.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'No permission.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Not authenticated.'
                  }

    return JsonResponse(answer)


@csrf_protect
def completed_orders_add(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')
        operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')
        taxi_driver_group, taxi_driver_group_created = Group.objects.get_or_create(name='Taxi driver')

        if admin_group_created:
            admin_group.permissions.add(21)
            admin_group.permissions.add(22)
            admin_group.permissions.add(23)
            admin_group.permissions.add(24)
            admin_group.permissions.add(25)
            admin_group.permissions.add(26)
            admin_group.permissions.add(27)
            admin_group.permissions.add(28)
            admin_group.permissions.add(29)
            admin_group.permissions.add(30)
            admin_group.permissions.add(31)
            admin_group.permissions.add(32)

        if operator_group_created:
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)

        if taxi_driver_group_created:
            taxi_driver_group.permissions.add(27)
            taxi_driver_group.permissions.add(28)
            taxi_driver_group.permissions.add(29)

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists() or
                request.user.groups.filter(name='Taxi driver').exists()
        ):
            if request.method == 'POST':
                parameters = dict(json.loads(request.body))

                if (('taxi driver' in parameters) and
                        ('opening time' in parameters) and
                        ('closing time' in parameters) and
                        ('starting address' in parameters) and
                        ('final address' in parameters) and
                        ('price' in parameters) and
                        (len(parameters) == 6)
                ):
                    order = CompletedOrders(taxi_driver=parameters['taxi driver'],
                                            opening_time=datetime.datetime(*list(map(int, parameters['opening time'].split()))),
                                            closing_time=datetime.datetime(*list(map(int, parameters['closing time'].split()))),
                                            starting_address=parameters['starting address'],
                                            final_address=parameters['final address'],
                                            price=float(parameters['price'])
                                            )
                    order.save()

                    answer = {'Status': 'Success',
                              'Message': 'Created.'
                              }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Wrong parameters.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Wrong method.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'No permission.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Not authenticated.'
                  }

    return JsonResponse(answer)
