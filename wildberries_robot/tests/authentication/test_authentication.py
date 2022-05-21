import pytest
import json
from django.urls import reverse
from django.contrib.auth import get_user_model
from authentication.models import User


@pytest.mark.parametrize('url', [
    ('registration'),
    ('login'),
])
@pytest.mark.django_db
def test_get_method_for_url(client_api, url):
    response = client_api.get(reverse(url))
    assert response.status_code == 405


@pytest.mark.django_db
def test_published_post_register(client_api, user_data):
    response = client_api.post(
        reverse('registration'), data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201
    assert response.data['email'] == user_data['email']
    assert response.data['username'] == user_data['username']


@pytest.mark.django_db
def test_login_user(client_api, create_user, user_data):
    response = client_api.post(reverse('login'), data=json.dumps(
        user_data), content_type='application/json')
    assert response.status_code == 200
    assert response.data['token'] is not None
    assert response.is_rendered == True
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser(email='test_superuser@test.com', username='super_user',
                                               password='superuser', )
    assert admin_user.is_active == True
    assert admin_user.is_staff == True
    assert admin_user.is_superuser == True


@pytest.mark.django_db
def test_published_post_register_wthout_email(client_api):
    data = {
        "email": "",
        "username": "john",
        "password": "Hack1234",
        "confirm_password": "Hack1234",
    }
    response = client_api.post(
        reverse('registration'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['email'][0].title(
    ) == 'Это Поле Не Может Быть Пустым.'
    print(response.data['email'][0].title())


@pytest.mark.django_db
def test_published_post_register_without_username(client_api):
    data = {
        "email": "lennon@thebeatles.com",
        "username": "",
        "password": "Hack1234",
        "confirm_password": "Hack1234",
    }
    response = client_api.post(
        reverse('registration'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['username'][0].title(
    ) == 'Это Поле Не Может Быть Пустым.'


@pytest.mark.django_db
def test_published_post_register_without_password(client_api):
    data = {
        "email": "lennon@thebeatles.com",
        "username": "john",
        "password": "",
        "confirm_password": "",
    }
    response = client_api.post(
        reverse('registration'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['password'][0].title(
    ) == 'Это Поле Не Может Быть Пустым.'
    assert response.data['confirm_password'][0].title(
    ) == 'Это Поле Не Может Быть Пустым.'


@pytest.mark.django_db
def test_published_post_register_passwords_do_not_match(client_api):
    data = {
        "email": "lennon@thebeatles.com",
        "username": "john",
        "password": "Hack1234",
        "confirm_password": "124Hack",
    }
    response = client_api.post(
        reverse('registration'), data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.data['password'][0].title(
    ) == "Password И Confirm Password Don'T Match!"
    assert response.data['confirm_password'][0].title(
    ) == "Password И Confirm Password Don'T Match!"
