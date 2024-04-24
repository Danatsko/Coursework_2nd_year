import json

from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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