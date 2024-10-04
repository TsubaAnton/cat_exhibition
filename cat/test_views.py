import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Cat, Breed, Rating
from users.models import User
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(email='test@test.com', password='12345678')


@pytest.fixture
def breed(db):
    return Breed.objects.create(breed='Sphinx')


@pytest.fixture
def cat(db, user, breed):
    return Cat.objects.create(name='Тест', color='Рыжий', age_months=10, description='Рыжий Тест', owner=user, breed=breed)


@pytest.mark.django_db
def test_cat_list(api_client, user):
    token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get(reverse('cat:cat_list'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cat_create(api_client, user, breed):
    api_client.force_authenticate(user=user)
    data = {'name': 'Борис', 'color': 'Черный', 'age_months': 20, 'description': 'Черный Борис', 'owner': user.id, 'breed': breed.id}
    response = api_client.post(reverse('cat:cat_create'), data=data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_cat_retrieve(api_client, user, cat):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('cat:cat_retrieve', kwargs={'pk': cat.pk}))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cat_update(api_client, user, cat):
    api_client.force_authenticate(user=user)
    data = {'name': 'Мурзик'}
    response = api_client.patch(reverse('cat:cat_update', kwargs={'pk': cat.pk}), data=data, format='json')
    assert response.status_code == status.HTTP_200_OK
    cat.refresh_from_db()
    assert cat.name == 'Мурзик'


@pytest.mark.django_db
def test_cat_destroy(api_client, user, cat):
    api_client.force_authenticate(user=user)
    response = api_client.delete(reverse('cat:cat_destroy', kwargs={'pk': cat.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_breed_list(api_client, user, breed):
    api_client.force_authenticate(user=user)
    response = api_client.get(reverse('cat:breed_list'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_rating_create(api_client, user, cat):
    api_client.force_authenticate(user=user)
    data = {'cat': cat.id, 'score': '5'}
    response = api_client.post(reverse('cat:rating_create'), data=data, format='json')
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Rating.objects.count() == 1
    assert Rating.objects.get().score == 5
    cat.refresh_from_db()
    assert cat.ratings_score == 5.0
