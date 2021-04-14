from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)

from rest_framework_simplejwt.authentication import JWTAuthentication

import functools

SETTINGS_USERS = settings.SETTINGS_USERS

def checkParamsJson(_func=None, *, listParams=[]):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_check_token(*args, **kwargs):
            paramsDict = args[1].data
            for param in listParams:
                try:
                    tempParamData = paramsDict[param]
                except:
                    msg = f"{' or '.join(listParams)}"
                    if len(listParams) > 1:
                        msg +=  " dont exist."
                    else:
                        msg +=  " does not exist."
                    return Response({"msg": msg}, status=HTTP_400_BAD_REQUEST)
            return func(*args, **kwargs)
        return wrapper_check_token

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

def get_user_from_request(self, request):
    header = JWTAuthentication.get_header(self, request)
    raw_token = JWTAuthentication.get_raw_token(self, header)
    validated_token = JWTAuthentication.get_validated_token(self, raw_token)
    user = JWTAuthentication.get_user(self, validated_token)
    return user

def checkPermissions(_func=None, *, permission=0):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_check_token(*args, **kwargs):
            if (permission != 0) and (permission > get_user_from_request(HelloView.get, args[1]).profile.permission):
                return Response({"msg": "Permission is required"}, status=HTTP_400_BAD_REQUEST)
            # print(get_user_from_request(HelloView.get, args[1]), permission)
            return func(*args, **kwargs)
        return wrapper_check_token

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

def sendMail(listEmailsToSend, title, data):
    """
        Sends an email according to a list of emails or a single email
        params: 
            list emails to send, 
            title of email,
            data of email,
        error:
            return response HTTP 400 Bad Request and return message.
    """
    if isinstance(listEmailsToSend, str):
        listEmailsToSend = [listEmailsToSend]
    send_mail(
        f'{title}',
        f'{data}',
        settings.EMAIL_HOST_USER,
        listEmailsToSend,
        fail_silently=False,
    )

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    @checkPermissions(permission=100)
    def get(self, request):
        user = get_user_from_request(self, request)
        content = {'message': 'Hello, World!'}
        return Response(content, status=HTTP_200_OK)