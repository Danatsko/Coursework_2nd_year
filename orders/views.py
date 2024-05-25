import datetime

from geopy.geocoders import Nominatim

from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from orders.models import (ActiveOrders,
                           CompletedOrders)


nominatim = Nominatim(user_agent='Program')


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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='Operator').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('opening time' in parameters) and
                        ('starting address' in parameters) and
                        ('final address' in parameters) and
                        (len(parameters) == 3)
                ):
                    if parameters['starting address']:
                        starting_address_data = nominatim.geocode(parameters['starting address']).raw
                        starting_address_coordinates = f'{starting_address_data["lat"]} {starting_address_data["lon"]}'
                    else:
                        starting_address_coordinates = ''

                    if parameters['final address']:
                        final_address_data = nominatim.geocode(parameters['final address']).raw
                        final_address_coordinates= f'{final_address_data["lat"]} {final_address_data["lon"]}'
                    else:
                        final_address_coordinates = ''

                    order = ActiveOrders(opening_time=datetime.datetime(*list(map(int, parameters['opening time'].split()))),
                                         starting_address=parameters['starting address'],
                                         starting_address_coordinates=starting_address_coordinates,
                                         final_address=parameters['final address'],
                                         final_address_coordinates=final_address_coordinates
                                         )
                    order.save()

                    answer = {'Status': 'Success',
                              'Message': 'Додано.'
                              }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if taxi_driver_group_created:
            taxi_driver_group.permissions.add(27)
            taxi_driver_group.permissions.add(28)
            taxi_driver_group.permissions.add(29)
            taxi_driver_group.permissions.add(33)
            taxi_driver_group.permissions.add(34)

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists() or
                request.user.groups.filter(name='Taxi driver').exists()
        ):
            if request.method == 'POST':
                parameters = request.POST

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
                              'Message': 'Додано.'
                              }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def active_orders_change_information(request):
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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='Operator').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('id' in parameters) and
                        ('new opening time' in parameters) and
                        ('new starting address' in parameters) and
                        ('new final address' in parameters) and
                        (len(parameters) == 4)
                ):
                    if ActiveOrders.objects.filter(id=parameters['id']).exists():
                        order = ActiveOrders.objects.get(id=parameters['id'])

                        if parameters['new opening time']:
                            order.opening_time = datetime.datetime(*list(map(int, parameters['new opening time'].split())))
                        if parameters['new starting address']:
                            new_starting_address_data = nominatim.geocode(parameters['new starting address']).raw

                            order.starting_address = parameters['new starting address']
                            order.starting_address_coordinates = f'{new_starting_address_data["lat"]} {new_starting_address_data["lon"]}'
                        if parameters['new final address']:
                            new_final_address_data = nominatim.geocode(parameters['new final address']).raw

                            order.final_address = parameters['new final address']
                            order.final_address_coordinates = f'{new_final_address_data["lat"]} {new_final_address_data["lon"]}'

                        order.save()

                        answer = {'Status': 'Success',
                                  'Message': 'Змінено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Активного замовлення не існує.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def completed_orders_change_information(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')

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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('id' in parameters) and
                        ('new taxi driver' in parameters) and
                        ('new opening time' in parameters) and
                        ('new closing time' in parameters) and
                        ('new starting address' in parameters) and
                        ('new final address' in parameters) and
                        ('new price' in parameters) and
                        (len(parameters) == 7)
                ):
                    if CompletedOrders.objects.filter(id=parameters['id']).exists():
                        order = CompletedOrders.objects.get(id=parameters['id'])

                        if parameters['new taxi driver']:
                            order.taxi_driver = parameters['new taxi driver']
                        if parameters['new opening time']:
                            order.opening_time = datetime.datetime(*list(map(int, parameters['new opening time'].split())))
                        if parameters['new closing time']:
                            order.closing_time = datetime.datetime(*list(map(int, parameters['new closing time'].split())))
                        if parameters['new starting address']:
                            order.starting_address = parameters['new starting address']
                        if parameters['new final address']:
                            order.final_address = parameters['new final address']
                        if parameters['new price']:
                            order.price = float(parameters['new price'])

                        order.save()

                        answer = {'Status': 'Success',
                                  'Message': 'Змінено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Завершеного замовлення не існує.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def active_orders_delete(request):
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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if taxi_driver_group_created:
            taxi_driver_group.permissions.add(27)
            taxi_driver_group.permissions.add(28)
            taxi_driver_group.permissions.add(29)
            taxi_driver_group.permissions.add(33)
            taxi_driver_group.permissions.add(34)

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists() or
                request.user.groups.filter(name='Taxi driver').exists()
        ):
            if request.method == 'POST':
                parameters = request.POST

                if (('id' in parameters) and
                        (len(parameters) == 1)
                ):
                    if ActiveOrders.objects.filter(id=parameters['id']).exists():
                        order = ActiveOrders.objects.get(id=parameters['id'])
                        order.delete()

                        answer = {'Status': 'Success',
                                  'Message': 'Видалено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Активного замовлення не існує.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def completed_orders_delete(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')

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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('id' in parameters) and
                        (len(parameters) == 1)
                ):
                    if CompletedOrders.objects.filter(id=parameters['id']).exists():
                        order = CompletedOrders.objects.get(id=parameters['id'])
                        order.delete()

                        answer = {'Status': 'Success',
                                  'Message': 'Видалено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Завершеного замовлення не існує.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Неправильні параметри.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def active_orders_view(request):
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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if taxi_driver_group_created:
            taxi_driver_group.permissions.add(27)
            taxi_driver_group.permissions.add(28)
            taxi_driver_group.permissions.add(29)
            taxi_driver_group.permissions.add(33)
            taxi_driver_group.permissions.add(34)

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists() or
                request.user.groups.filter(name='Taxi driver').exists()
        ):
            if request.method == 'GET':
                answer = {}
                orders = ActiveOrders.objects.all()

                for order in orders:
                    information = {'opening time': order.opening_time,
                                   'starting address': order.starting_address,
                                   'starting address coordinates': order.starting_address_coordinates,
                                   'final address': order.final_address,
                                   'final address coordinates': order.final_address_coordinates
                                   }

                    answer[order.id] = information
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def completed_orders_view(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')
        operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')
        spectator_group, spectator_group_created = Group.objects.get_or_create(name='Spectator')

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
            admin_group.permissions.add(33)
            admin_group.permissions.add(34)
            admin_group.permissions.add(35)
            admin_group.permissions.add(36)

        if operator_group_created:
            operator_group.permissions.add(24)
            operator_group.permissions.add(25)
            operator_group.permissions.add(26)
            operator_group.permissions.add(27)
            operator_group.permissions.add(28)
            operator_group.permissions.add(29)
            operator_group.permissions.add(32)
            operator_group.permissions.add(36)

        if spectator_group_created:
            spectator_group.permissions.add(32)

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists() or
                request.user.groups.filter(name='Spectator').exists()
        ):
            if request.method == 'GET':
                answer = {}
                orders = CompletedOrders.objects.all()

                for order in orders:
                    information = {'taxi driver': order.taxi_driver,
                                   'opening time': order.opening_time,
                                   'closing time': order.closing_time,
                                   'starting address': order.starting_address,
                                   'final address': order.final_address,
                                   'price': order.price
                                   }

                    answer[order.id] = information
            else:
                answer = {'Status': 'Fail',
                          'Message': 'Неправильний метод.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Немає дозволу.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)