from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import secrets
# from .views import sendMail

from django.conf import settings
SETTINGS_USERS = settings.SETTINGS_USERS

class TokenRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, default='')
    create_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.user.username} {self.token}'

    def __repr__(self):
        return f'{self.user.username} {self.token}'

    @classmethod
    def create(self, user):
        token = secrets.token_hex(SETTINGS_USERS['TOKEN_REGISTER_LENGTH'])
        tokenRegister = self(user=user, token=token)
        return tokenRegister


class TokenChangePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, default='')
    create_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.user.username} {self.token}'

    def __repr__(self):
        return f'{self.user.username} {self.token}'

    @classmethod
    def create(self, user):
        token = secrets.token_hex(SETTINGS_USERS['TOKEN_CHANGE_PASSWORD_LENGTH'])
        tokenChangePassword = self(user=user, token=token)
        return tokenChangePassword

class Profile(models.Model):
    regular_code = 100
    manager_code = 200

    Permissions = [
        (regular_code, 'regular'),
        (manager_code, 'manager')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_login = models.BooleanField(default=False)

    is_approved = models.BooleanField(default=False)
    permission = models.IntegerField(choices=Permissions, default=regular_code)
    count_login_now = models.PositiveIntegerField(default=0)
    last_login_date = models.DateTimeField(default=timezone.now, blank=True)
    registration_date = models.DateTimeField(default=timezone.now, blank=True)

    @classmethod
    def create(self, user):
        tokenRegister = TokenRegister.create(user=user)
        tokenRegister.save()

        profile = self(user=user)
        return profile

    def __str__(self):
        return f'{self.user.username}'

    def __repr__(self):
        return f'{self.user.username}'
