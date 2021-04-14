from django.contrib import admin
from .models import Profile, TokenRegister, TokenChangePassword

admin.site.register(TokenRegister)
admin.site.register(TokenChangePassword)
admin.site.register(Profile)
