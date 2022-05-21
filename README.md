# wildberries_statistics

Приложение, которое помогает автоматически отслеживать динамику изменения параметров карточки товара на
маркетплейсе Wildberries (далее Карточка), получать по запросу статистическую
информацию о состоянии параметров Карточки в заданном диапазоне дат с
заданным временным интервалом (не чаще 1 записи в час).

Для реализации использовался следующий стэк

```
- sqlparse
- beautifulsoup4
- coreapi
- coreschema
- Django>
- djangorestframework
- djangorestframework-simplejwt
- drf-yasg
- django-annoying
- django-celery-beat
- django-ckeditor
- django-cors-headers
- django-js-asset
- django-ranged-response
- django-templated-mail
- django-taggit
- gunicorn
- Jinja2
- lxml
- pip-compile-multi
- pyjwt
- psycopg2
- psycopg2-binary
- pytest
- pytest-cov
- pytest-django
- python-dateutil
- python-dotenv
- requests
- selenium
- celery
- redis
- flower
- webdriver-manager
```

## Установка и запуск(локально):

1. Скачать проект

   - git clone https://github.com/scad89/wildberries_statistics.git

2. Добавить файл с переменными окружения(.env) в корень проекта

3. Активировать виртуальное окружение:

   - . venv_name/Scripts/activate - Windows
   - source venv_name/bin/activate - Linux

4. Установить зависимости(в виртуальном окружении):

   - pip install -r requirements.txt
   - pip-compile -U

5. Сделать миграции:

   - python manage.py makemigrations
   - python manage.py migrate

6. Запустить сервер:

   - python manage.py runserver

7. Запустить Celery в отдельном терминале:

   - celery -A wildberries_robot worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info

8. Запустить flower в отдельном терминале:

- celery -A notification_service flower --port=5555

```
http://127.0.0.1:8000 - все доступные маршруты
http://127.0.0.1:5555 -по этому адресу можно открыть flower
```

## Установка и запуск(docker-compose):

1. Добавить файл с переменными окружения(.env_docker) в корень проекта
2. Запустить командой:

```
   - sudo docker-compose up -d
```

Если необходимо пересобрать контейнеры(внесли какие-то изменения) использовать:

```
   - sudo docker-compose up --build
```

Если Вы запускаете проект на Windows, а docker из-под виртуальной машины(по типу VirtualBox), проект
по адресу 0.0.0.0:8000 может не открыться. Тогда необходимо использовать адрес 192.168.99.100:8000

Для остановки контейнеров используйте команду:

```
   - docker-compose down
```

- http://0.0.0.0:8000/api/v1/registration/ - регистрация нового пользователя
- http://0.0.0.0:8000/api/v1/login/ - авторизация зарегестрированного пользователя
- http://0.0.0.0:8000/api/v1/logout - выход авторизированного пользователя
- http://0.0.0.0:8000/api/v1/article/ - добавить новый артикул/ получить список всех артикулов
- http://0.0.0.0:8000/api/v1/article/1/ - детальная информация о артикуле/обновление артикула/удаление артикула
- http://0.0.0.0:8000/api/v1/statistics/1/?start=2022-05-13&end=2022-05-18&interval=1 - получение статистики с заданным временным диапазоном и заданным интервалом
- http://0.0.0.0:8000/docs/ - документация

### Описание реализации:

- Пользователь имеет возможность зарегестрироваться в сервисе, указать логин, пароль и email(JWT);
- Пользователю доступна возможность редактировать список артикулов, которые он указал;
- Пользователь имеет возможность указать артикул товара, дату начала периода, дату окончания периода, интервал и получить в соответствии с заданными параметрами историческую информацию о параметрах данных полученных из маркетплейса;
- Данные, которые собираются в маркетплейсе следующие:
  - Наименование товара;
  - Цена без скидки;
  - Цена со скидкой;
  - Бренд;
  - Поставщик;
  - Артикул данных маркетплейса ссылается на артикул пользователя;
- Как только пользователь добавил артикул, запускается процесс сбора информации из маркетплейса с периодичность один раз в час;

### Тесты:

Запускать тесты командой:

```
   - pytest
```

## Contacts

- Instagram: [@igor*komkov*](https://www.instagram.com/igor_komkov_/)
- Vk.com: [Igor Komkov](https://vk.com/zzzscadzzz)
- Linkedin: [Igor Komkov](https://www.linkedin.com/in/igor-komkov/)
- email: **scad200@gmail.com**
- Telegram: **@zzzSCADzzz**
