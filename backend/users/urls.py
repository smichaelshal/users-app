from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import LoginApi, RegisterAPI, ConfirmedEmailApi, ResetPasswordApi, ChangePasswordApi, TestApi
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('confirmed-email/', ConfirmedEmailApi.as_view(), name='confirmed-email'),
    path('login/', LoginApi.as_view(), name='login'),
    path('reset-password/', ResetPasswordApi.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordApi.as_view(), name='change-password'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', TestApi.as_view(), name='test'),

    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('hello/', HelloView.as_view(), name='hello'),
]