from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserListAPIView(generics.ListAPIView):
    """Представление для вывода списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для создания пользователя"""
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для получения подробной информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для добавления и изменения информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Представление для удаления информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
