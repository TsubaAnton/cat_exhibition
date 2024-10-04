import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import User
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(email='test@test.com', password='12345678')


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(email='admin@test.com', password='87654321')


@pytest.mark.django_db
def test_user_list(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('users:user_list'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_create(api_client):
    data = {'email': 'user@test.com', 'password': '11112222'}
    response = api_client.post(reverse('users:user_create'), data=data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_retrieve(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('users:user_retrieve', kwargs={'pk': user.pk}))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_update(api_client, user):
    api_client.force_authenticate(user=user)
    data = {'email': 'update@test.com'}
    response = api_client.patch(reverse('users:user_update', kwargs={'pk': user.pk}), data=data, format='json')
    assert response.status_code == status.HTTP_200_OK
    user.refresh_from_db()
    assert user.email == 'update@test.com'


@pytest.mark.django_db
def test_user_destroy(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.delete(reverse('users:user_destroy', kwargs={'pk': user.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
