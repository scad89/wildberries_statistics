import pytest
import json
from pytest_django.asserts import assertRaisesMessage
from cards.models import UserArticle

URL_ARTICLE = '/api/v1/article/'


@pytest.mark.django_db
def test_get_method_for_url_no_authorized_user(data_article, client_api):
    response = client_api.get(URL_ARTICLE, content_type='application/json')
    assert response.status_code == 401
    assert response.status_text == 'Unauthorized'


@pytest.mark.django_db
def test_post_method_for_url_no_authorized_user(data_article, client_api):
    response = client_api.post(URL_ARTICLE, content_type='application/json')
    assert response.status_code == 401
    assert response.status_text == 'Unauthorized'


@pytest.mark.django_db
def test_get_method_for_statistics_no_authorized_user(data_record, client_api):
    response = client_api.get(
        '/api/v1/statistics/1/?start=2022-05-13&end=2022-05-29&interval=1',
        content_type='application/json')
    assert response.status_code == 401
    assert response.status_text == 'Unauthorized'


@pytest.mark.django_db
def test_get_method_for_url_authorized_user(data_article, authenticated_user):
    response = authenticated_user.get(
        URL_ARTICLE, content_type='application/json')
    data = dict(response.data['results'][0])
    assert response.status_code == 200
    assert type(data['article']) is int
    assert data_article.article == data['article']


@pytest.mark.django_db
def test_post_method_for_url_authorized_user(data_article, authenticated_user):
    data = {'article': 38336999}
    response = authenticated_user.post(
        URL_ARTICLE, data=json.dumps(data), content_type='application/json')
    last_save_article = UserArticle.objects.all().last()
    assert response.status_code == 201
    assert last_save_article.article == response.data['article']
    assert type(response.data['article']) is int


@pytest.mark.django_db
def test_get_method_for_statistics_url_authorized_user(data_record, authenticated_user):
    response = authenticated_user.get('/api/v1/statistics/1/?start=2022-05-13&end=2022-05-29&interval=1',
                                      content_type='application/json')
    assert response.status_code == 200
    assert response.status_text == 'OK'


@pytest.mark.django_db
def test_post_without_data_in_article(authenticated_user):
    response = authenticated_user.post(URL_ARTICLE, {'article': ''})
    assert response.status_code == 400
    assert response.data['article'][0].title() == 'Введите Правильное Число.'


@pytest.mark.django_db
def test_post_with_invalid_key_in_article(authenticated_user):
    authenticated_user.post(URL_ARTICLE,
                            {'invalid_key': 38336383})
    with assertRaisesMessage(UserArticle.DoesNotExist, 'UserArticle matching query does not exist.'):
        UserArticle.objects.get(article='38336383')


@pytest.mark.django_db
def test_post_with_nonexistent_section_in_add_new_section(authenticated_user):
    authenticated_user.get(URL_ARTICLE)
    with assertRaisesMessage(UserArticle.DoesNotExist, 'UserArticle matching query does not exist.'):
        UserArticle.objects.get(id=15)
