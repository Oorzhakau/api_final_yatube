# api_final
### Описание:
Проект реализации API социальной сети Yatupe.
Благодаря данному API клиент может:
1. Аутентифицироваться по токену;
2. Добавлять/удалять/редактировать посты;
3. Добавлять/удалять/редактировать комментарии;
4. Подписываться к автору.
### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Oorzhakau/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:

1. Request: POST http://127.0.0.1:8000/api/v1/jwt/create/
>{
>    "username": "user1",
>    "password": "qwerty_123"
>}
Response: 
>{
>    "refresh": "string",
>    "access": "string"
>}
2. Request: POST http://127.0.0.1:8000/api/v1/posts/
>{
>    "text": "Текст тестового поста 5 User 1"
>}
3. Request: GET http://127.0.0.1:8000/api/v1/posts/
Response: 
>{
>    "count": 123,
>    "next": "http://api.example.org/accounts/?offset=400&limit=100",
>    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
>    "results": [
>        {
>            "id": 0,
>            "author": "string",
>            "text": "string",
>            "pub_date": "2021-10-14T20:41:29.648Z",
>            "image": "string",
>            "group": 0
>        }
>    ]
>}
4. Request: POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Response:
>{
>    "id": 0,
>    "author": "string",
>    "text": "string",
>    "created": "2019-08-24T14:15:22Z",
>    "post": 0
>}
5. Request: GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Response:
>{
>    "id": 0,
>    "author": "string",
>    "text": "string",
>    "created": "2019-08-24T14:15:22Z",
>    "post": 0
>}
5. Request: GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
Response:
>{
>    "id": 0,
>    "author": "string",
>    "text": "string",
>   "created": "2019-08-24T14:15:22Z",
>    "post": 0
>}