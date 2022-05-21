import pytest
import pytz
from datetime import datetime
from cards.models import UserArticle, RecordCard
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def client_api():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        "email": "lennon@thebeatles.com",
        "username": "john",
        "password": "Hack1234",
        "confirm_password": "Hack1234",
    }


@pytest.fixture
def data_article():
    return UserArticle.objects.create(article=38336383)


@pytest.fixture
def data_record(data_article):
    date = '2022-05-18'
    str_of_time = datetime.strptime(date, '%Y-%m-%d')
    timezone_time = pytz.utc.localize(str_of_time, is_dst=None).astimezone()
    date_time_utc = timezone_time.replace(minute=0, second=0, microsecond=0)
    return RecordCard.objects.create(
        id_article=data_article,
        name_of_product="sneakers",
        price_without_discount=4500,
        price_with_discount=3825,
        brand="Nike",
        supplier="NikeCorp",
        record_time=date_time_utc)


@pytest.fixture()
def create_user():
    User = get_user_model()
    return User.objects.create_user(
        'john', 'lennon@thebeatles.com', 'Hack1234')


@pytest.fixture
def auth_user(create_user):
    User = get_user_model()
    user = User.objects.get(username='john')
    client = APIClient()
    return client.force_authenticate(user=user)


@pytest.fixture
def authenticated_user(create_user):
    client = APIClient()
    refresh = RefreshToken.for_user(create_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client
