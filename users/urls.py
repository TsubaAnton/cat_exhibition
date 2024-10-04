from .apps import UsersConfig
from django.urls import path
from .views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user_destroy'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
