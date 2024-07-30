# api_yatube
api_yatube
# Project Name

## Описание проекта

Этот проект представляет собой API для работы с постами, группами и комментариями. Он позволяет создавать, читать, обновлять и удалять посты и комментарии, а также просматривать группы.

## Как развернуть проект

### Требования

- Python 3.8+
- Django 3.2+
- Django REST framework 3.12+
- SQLite (или другой поддерживаемый Django баз данных)

### У

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:
    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:
 ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

### Использование

После запуска сервера, API будет доступен по адресу `http://127.0.0.1:8000/`.

## Примеры запросов и ответов

### Получение списка постов

**Запрос:**
```http
GET /v1/posts/

**Ответ:**

Json
Insert code

[
    {
        "id": 1,
        "text": "Первый пост",
        "pub_date": "2023-10-01T12:00:00Z",
       author": "username",
        "image": null,
        "group": "group-slug"
    },
    ...
]

### Создание нового поста

**Запрос:**

Http
Insert code

POST /v1/posts/
Content-Type: application/json
Authorization: Token your_token

{
    "text": "Новый пост",
    "group": "group-slug"
}

**Ответ:**

Json
Insert code

{
    "id": 2,
    "text": "Новый пост",
    "pub_date": "2023-10-01T12:30:00Z",
    "author": "username",
    "image": null,
    "group": "group-slug
}

Информация об авторе
Автор: Лавреников Константин