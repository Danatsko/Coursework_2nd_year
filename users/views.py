import datetime

from django.contrib.auth import (authenticate,
                                 login,
                                 get_user_model,
                                 logout
                                 )
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import (csrf_exempt,
                                          csrf_protect
                                          )

from users.models import TaxiDriversCoordinates


def admin_group_add_permissions():
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


def operator_group_add_permissions():
    operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')

    if operator_group_created:
        operator_group.permissions.add(24)
        operator_group.permissions.add(25)
        operator_group.permissions.add(26)
        operator_group.permissions.add(27)
        operator_group.permissions.add(28)
        operator_group.permissions.add(29)
        operator_group.permissions.add(32)
        operator_group.permissions.add(36)


def taxi_driver_group_add_permissions():
    taxi_driver_group, taxi_driver_group_created = Group.objects.get_or_create(name='Taxi driver')

    if taxi_driver_group_created:
        taxi_driver_group.permissions.add(27)
        taxi_driver_group.permissions.add(28)
        taxi_driver_group.permissions.add(29)
        taxi_driver_group.permissions.add(33)
        taxi_driver_group.permissions.add(34)


def spectator_group_add_permissions():
    spectator_group, spectator_group_created = Group.objects.get_or_create(name='Spectator')

    if spectator_group_created:
        spectator_group.permissions.add(32)


@csrf_protect
def user_registration(request):
    if request.user.is_authenticated:
        admin_group_add_permissions()

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('username' in parameters) and
                        ('password' in parameters) and
                        ('status' in parameters) and
                        ('first name' in parameters) and
                        ('patronymic' in parameters) and
                        ('last name' in parameters) and
                        ('sex' in parameters) and
                        ('date of birth' in parameters) and
                        ('email' in parameters) and
                        ('phone number' in parameters) and
                        (len(parameters) == 10)
                ):
                    if get_user_model().objects.filter(username=parameters['username']).exists() == False:
                        try:
                            user = get_user_model().objects.create_user(username=parameters['username'],
                                                                        first_name=parameters['first name'],
                                                                        patronymic=parameters['patronymic'],
                                                                        last_name=parameters['last name'],
                                                                        sex=parameters['sex'],
                                                                        date_of_birth=datetime.date(*list(map(int,parameters['date of birth'].split()))),
                                                                        email=parameters['email'],
                                                                        phone_number=parameters['phone number']
                                                                        )
                        except:
                            answer = {'Status': 'Fail',
                                      'Message': 'День народження введено некоректно.'
                                      }

                            return JsonResponse(answer)


                        user.set_password(raw_password=parameters['password'])
                        user.save()

                        admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')
                        operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')
                        taxi_driver_group, taxi_driver_group_created = Group.objects.get_or_create(name='Taxi driver')
                        spectator_group, spectator_group_created = Group.objects.get_or_create(name='Spectator')

                        admin_group_add_permissions()
                        operator_group_add_permissions()
                        taxi_driver_group_add_permissions()
                        spectator_group_add_permissions()

                        match parameters['status']:
                            case 'Admin':
                                user.groups.add(admin_group)
                            case 'Operator':
                                user.groups.add(operator_group)
                            case 'Taxi driver':
                                user.groups.add(taxi_driver_group)

                                taxi_driver_coordinates = TaxiDriversCoordinates(taxi_driver_id=user.id,
                                                                                 taxi_driver_status='Офлайн',
                                                                                 taxi_driver_coordinates=''
                                                                                 )
                                taxi_driver_coordinates.save()
                            case 'Spectator':
                                user.groups.add(spectator_group)

                        answer = {'Status': 'Success',
                                  'Message': 'Зареєстровано.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Користувач існує.'
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
def user_change_information(request):
    if request.user.is_authenticated:
        admin_group_add_permissions()

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('username' in parameters) and
                        ('new username' in parameters) and
                        ('new password' in parameters) and
                        ('new status' in parameters) and
                        ('new first name' in parameters) and
                        ('new patronymic' in parameters) and
                        ('new last name' in parameters) and
                        ('new sex' in parameters) and
                        ('new date of birth' in parameters) and
                        ('new email' in parameters) and
                        ('new phone number' in parameters) and
                        (len(parameters) == 11)
                ):
                    if get_user_model().objects.filter(username=parameters['username']).exists():
                        user = get_user_model().objects.get(username=parameters['username'])

                        if parameters['new username']:
                            if get_user_model().objects.filter(username=parameters['new username']).exists():
                                answer = {'Status': 'Fail',
                                          'Message': 'Користувач з таким нікнеймом існує.'
                                          }

                                return JsonResponse(answer)
                            else:
                                user.username = parameters['new username']
                        if parameters['new first name']:
                            user.first_name = parameters['new first name']
                        if parameters['new patronymic']:
                            user.patronymic = parameters['new patronymic']
                        if parameters['new last name']:
                            user.last_name = parameters['new last name']
                        if parameters['new sex']:
                            user.sex = parameters['new sex']
                        if parameters['new date of birth']:
                            try:
                                user.date_of_birth = datetime.date(*list(map(int, parameters['new date of birth'].split())))
                            except:
                                answer = {'Status': 'Fail',
                                          'Message': 'День народження введено некоректно.'
                                          }

                                return JsonResponse(answer)
                        if parameters['new email']:
                            user.email = parameters['new email']
                        if parameters['new phone number']:
                            user.phone_number = parameters['new phone number']
                        if parameters['new password']:
                            user.set_password(raw_password=parameters['new password'])

                        user.save()

                        if parameters['new status']:
                            admin_group, admin_group_created = Group.objects.get_or_create(name='Admin')
                            operator_group, operator_group_created = Group.objects.get_or_create(name='Operator')
                            taxi_driver_group, taxi_driver_group_created = Group.objects.get_or_create(name='Taxi driver')
                            spectator_group, spectator_group_created = Group.objects.get_or_create(name='Spectator')

                            admin_group_add_permissions()
                            operator_group_add_permissions()
                            taxi_driver_group_add_permissions()
                            spectator_group_add_permissions()

                            if user.groups.filter(name='Admin').exists():
                                user.groups.remove(admin_group)
                            elif user.groups.filter(name='Operator').exists():
                                user.groups.remove(operator_group)
                            elif user.groups.filter(name='Taxi driver').exists():
                                user.groups.remove(taxi_driver_group)

                                taxi_driver_coordinates = TaxiDriversCoordinates.objects.get(taxi_driver_id=user.id)
                                taxi_driver_coordinates.delete()
                            elif user.groups.filter(name='Spectator').exists():
                                user.groups.remove(spectator_group)

                            match parameters['new status']:
                                case 'Admin':
                                    user.groups.add(admin_group)
                                case 'Operator':
                                    user.groups.add(operator_group)
                                case 'Taxi driver':
                                    user.groups.add(taxi_driver_group)

                                    taxi_driver_coordinates = TaxiDriversCoordinates(taxi_driver_id=user.id,
                                                                                     taxi_driver_status='Офлайн',
                                                                                     taxi_driver_coordinates=''
                                                                                     )
                                    taxi_driver_coordinates.save()
                                case 'Spectator':
                                    user.groups.add(spectator_group)

                        answer = {'Status': 'Success',
                                  'Message': 'Змінено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Користувача не існує.'
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
def user_delete(request):
    if request.user.is_authenticated:
        admin_group_add_permissions()

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = request.POST

                if (('username' in parameters) and
                        (len(parameters) == 1)
                ):
                    if get_user_model().objects.filter(username=parameters['username']).exists():
                        user = get_user_model().objects.get(username=parameters['username'])

                        if user.groups.filter(name='Taxi driver').exists():
                            taxi_driver_coordinates = TaxiDriversCoordinates.objects.get(taxi_driver_id=user.id)
                            taxi_driver_coordinates.delete()

                        user.delete()

                        answer = {'Status': 'Success',
                                  'Message': 'Видалено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Користувача не існує.'
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
def users_view(request):
    if request.user.is_authenticated:
        admin_group_add_permissions()
        operator_group_add_permissions()

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Operator').exists()
        ):
            if request.method == 'GET':
                answer = {}
                users = get_user_model().objects.all()

                for user in users:
                    status = ''

                    if user.groups.filter(name='Admin').exists():
                        status = 'Admin'
                    elif user.groups.filter(name='Operator').exists():
                        status = 'Operator'
                    elif user.groups.filter(name='Taxi driver').exists():
                        status = 'Taxi driver'
                        taxi_driver_coordinates = TaxiDriversCoordinates.objects.get(taxi_driver_id=user.id)
                    elif user.groups.filter(name='Spectator').exists():
                        status = 'Spectator'

                    if status == 'Taxi driver':
                        information = {'username': user.username,
                                       'status': status,
                                       'first name': user.first_name,
                                       'patronymic': user.patronymic,
                                       'last name': user.last_name,
                                       'sex': user.sex,
                                       'date of birth': user.date_of_birth,
                                       'email': user.email,
                                       'phone number': user.phone_number,
                                       'online status': taxi_driver_coordinates.taxi_driver_status,
                                       'coordinates': taxi_driver_coordinates.taxi_driver_coordinates
                                       }
                    else:
                        information = {'username': user.username,
                                       'status': status,
                                       'first name': user.first_name,
                                       'patronymic': user.patronymic,
                                       'last name': user.last_name,
                                       'sex': user.sex,
                                       'date of birth': user.date_of_birth,
                                       'email': user.email,
                                       'phone number': user.phone_number,
                                       }

                    answer[user.username] = information
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
def taxi_driver_coordinates_change_information(request):
    if request.user.is_authenticated:
        admin_group_add_permissions()
        taxi_driver_group_add_permissions()

        if (request.user.groups.filter(name='Admin').exists() or
                request.user.groups.filter(name='Taxi driver').exists()
        ):
            if request.method == 'POST':
                parameters = request.POST

                if (('id' in parameters) and
                        ('new online status' in parameters) and
                        ('new coordinates' in parameters) and
                        (len(parameters) == 3)
                ):
                    if request.user.groups.filter(name='Taxi driver').exists():
                        taxi_driver_coordinates = TaxiDriversCoordinates.objects.get(taxi_driver_id=request.user.id)

                        taxi_driver_coordinates.taxi_driver_status = parameters['new online status']
                        taxi_driver_coordinates.taxi_driver_coordinates = parameters['new coordinates']

                        taxi_driver_coordinates.save()

                        answer = {'Status': 'Success',
                                  'Message': 'Змінено.'
                                  }
                    elif TaxiDriversCoordinates.objects.filter(taxi_driver_id=parameters['id']).exists():
                        taxi_driver_coordinates = TaxiDriversCoordinates.objects.get(taxi_driver_id=parameters['id'])

                        taxi_driver_coordinates.taxi_driver_status = parameters['new online status']
                        taxi_driver_coordinates.taxi_driver_coordinates = parameters['new coordinates']

                        taxi_driver_coordinates.save()

                        answer = {'Status': 'Success',
                                  'Message': 'Змінено.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Користувача не існує.'
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


@csrf_exempt
def user_login(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            parameters = request.POST

            if (('username' in parameters) and
                    ('password' in parameters) and
                    (len(parameters) == 2)
            ):
                if get_user_model().objects.filter(username=parameters['username']).exists():
                    user_authentication = authenticate(request,
                                                       username=parameters['username'],
                                                       password=parameters['password'],
                                                       )

                    if user_authentication:
                        login(request, user_authentication)

                        user_group = ''

                        if user_authentication.groups.filter(name='Admin').exists():
                            user_group = 'Admin'
                        elif user_authentication.groups.filter(name='Operator').exists():
                            user_group = 'Operator'
                        elif user_authentication.groups.filter(name='Taxi driver').exists():
                            user_group = 'Taxi driver'
                        elif user_authentication.groups.filter(name='Spectator').exists():
                            user_group = 'Spectator'

                        answer = {'Status': 'Success',
                                  'Message': 'Автентифіковано.',
                                  'User group': user_group
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Message': 'Неправильний пароль.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Message': 'Користувача не існує.'
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
                  'Message': 'Вже автентифіковано.'
                  }

    return JsonResponse(answer)


@csrf_protect
def user_logaut(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)

            answer = {'Status': 'Success',
                      'Message': 'Сесію закінчено.'
                      }
        else:
            answer = {'Status': 'Fail',
                      'Message': 'Неправильний метод.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Message': 'Не автентифіковано.'
                  }

    return JsonResponse(answer)
