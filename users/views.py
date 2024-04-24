import datetime
import json

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_protect
def user_registration(request):
    if request.user.is_authenticated:
        admin_group, admin_group_created = Group.objects.get_or_create(name="Admin")

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

        if request.user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                parameters = dict(json.loads(request.body))

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
                        user = get_user_model().objects.create_user(username=parameters['username'],
                                                                    first_name=parameters['first name'],
                                                                    patronymic=parameters['patronymic'],
                                                                    last_name=parameters['last name'],
                                                                    sex=parameters['sex'],
                                                                    date_of_birth=datetime.date(*list(map(int, parameters['date of birth'].split()))),
                                                                    email=parameters['email'],
                                                                    phone_number=parameters['phone number']
                                                                    )
                        user.set_password(raw_password=parameters['password'])
                        user.save()

                        match parameters['status']:
                            case 'Admin':
                                admin_group, admin_group_created = Group.objects.get_or_create(name="Admin")

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

                                user.groups.add(admin_group)
                            case 'Operator':
                                operator_group, operator_group_created = Group.objects.get_or_create(name="Operator")

                                if operator_group_created:
                                    operator_group.permissions.add(25)
                                    operator_group.permissions.add(26)
                                    operator_group.permissions.add(27)
                                    operator_group.permissions.add(28)
                                    operator_group.permissions.add(29)
                                    operator_group.permissions.add(32)

                                user.groups.add(operator_group)
                            case 'Spectator':
                                spectator_group, spectator_group_created = Group.objects.get_or_create(name="Spectator")

                                if spectator_group_created:
                                    spectator_group.permissions.add(32)

                                user.groups.add(spectator_group)

                        answer = {'Status': 'Success',
                                  'Massage': 'Created.'}
                    else:
                        answer = {'Status': 'Fail',
                                  'Massage': 'User exists.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Massage': 'Wrong parameters.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Massage': 'Wrong method.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Massage': 'No permission.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Massage': 'Not authenticated.'
                  }

    return JsonResponse(answer)


@csrf_exempt
def user_login(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            parameters = dict(json.loads(request.body))

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

                        answer = {'Status': 'Success',
                                  'Massage': 'Login.'
                                  }
                    else:
                        answer = {'Status': 'Fail',
                                  'Massage': 'Wrong password.'
                                  }
                else:
                    answer = {'Status': 'Fail',
                              'Massage': 'User does not exist.'
                              }
            else:
                answer = {'Status': 'Fail',
                          'Massage': 'Wrong parameters.'
                          }
        else:
            answer = {'Status': 'Fail',
                      'Massage': 'Wrong method.'
                      }
    else:
        answer = {'Status': 'Fail',
                  'Massage': 'Authenticated.'
                  }

    return JsonResponse(answer)