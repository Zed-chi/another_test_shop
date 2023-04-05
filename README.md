# Тестовое для проекта Сарафан

### Cсылка на само задание - [тут](https://docs.google.com/document/d/1ijSd6t5pSGELWKnvswsKViuVC9fISAeG5J54BHO5W5U)

### 1. Консольная программа

Запуск `python task.py -n <число>`

### 2. Джанго проект

1. для token-based регистрации нужно отправить POST запрос на `/auth/users/` json формата:
```json
{	
	"name":"...",
	"email":"...",
	"password":"..."
}
```
После этого получаем в ответ json:
```json
{
	"name": "...",
	"email": "...",
	"id": ...
}
```

2. Для token-based входа отправить POST запрос на `/auth/token/login/` json формата:
```json
{	
	"email":"...",
	"password":"..."
}
```

После этого получаем в ответ json:
```json
{
	"auth_token": "fafcd0850707e93e930dbca087bce495d84501ca"
}
```

Далее для операций требующих авторизации добавляем заголовок
`Authorization: Token ...`


3. Для token-based выхода отправить POST запрос на  `/auth/token/logout/` c заголовком авторизации
