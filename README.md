# Тестовое для проекта Сарафан

### Cсылка на само задание - [тут](https://docs.google.com/document/d/1ijSd6t5pSGELWKnvswsKViuVC9fISAeG5J54BHO5W5U)

### 1. Консольная программа

Запуск `python task.py -n <число>`

### 2. Джанго проект

## Для запуска создать в директории джанго проекта файл `.env` и заполнить:
```
SECRET=...
STATIC_ROOT=...(например .)
STATIC_DIR=... (например "__static")
MEDIA_DIR=... (например "__media")
DEBUG=... (True/False)
```

### Для локальной установки:
1) установить зависимости (глобально или в виртуальном окружении):`pip install -r requirements.txt`
2) Провести первоначальную миграцию `python manage.py migrate`
3) Создать суперпользователя `python manage.py createsuperuser`
4) Запустить на тестовом сервере `python manage.py runserver` либо на uvicorn/gunicorn/hypercorn/uwsgi

### Для докер запуска:
1) Зайти в контейнер,
2) В папке приложения `python manage.py createsuperuser`


#### Для token-based регистрации нужно
- отправить POST запрос на `/auth/users/` json формата:
```json
{	
	"name":"...",
	"email":"...",
	"password":"..."
}
```
- После этого получаем в ответ json:
```json
{
	"name": "...",
	"email": "...",
	"id": ...
}
```

#### Для token-based входа 
- отправить POST запрос на `/auth/token/login/` json формата:
```json
{	
	"email":"...",
	"password":"..."
}
```

- После этого получаем в ответ json:
```json
{
	"auth_token": "..."
}
```

- Далее для операций требующих авторизации добавляем заголовок
`Authorization: Token ...`


#### Для token-based выхода 
- отправить POST запрос на  `/auth/token/logout/` c заголовком авторизации
