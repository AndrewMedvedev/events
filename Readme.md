# Документация REST API


## Сервис мероприятий 


## Базовый ендпоинт: '/events/'


## Add:
Ресурс для создания мероприятий.


> POST '/api/v1/events/add/'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| name_event | str |
| date_time | datetime |
| location | str |
| description | str |
| points_for_the_event | int |
| limit_people | int |


Пример ответа:
'{
  "message": 200
}'


## Get:
Ресурс для просмотра всех  мероприятий.


> GET '/api/v1/events/get/'


Ничего не принимает.


Пример ответа:
'[
  {
    "name_event": "dcsadcscsacd",
    "id": 1,
    "date_time": "2025-03-01T21:46:20.964000+00:00",
    "limit_people": 0,
    "location": "sacsdcsacs",
    "description": "csacsdcsacs",
    "points_for_the_event": 0
  },
  {
    "name_event": "saefsc s sa fsfs",
    "id": 2,
    "date_time": "2025-03-01T21:46:20.964000+00:00",
    "limit_people": 0,
    "location": "sacsdcsacs",
    "description": "csacsdcsacs",
    "points_for_the_event": 0
  },
  {
    "name_event": " vasd sav sakjndf klawsf",
    "id": 3,
    "date_time": "2025-03-01T21:46:20.964000+00:00",
    "limit_people": 0,
    "location": "sacsdcsacs",
    "description": "csacsdcsacs",
    "points_for_the_event": 0
  },
  {
    "name_event": "упмукмвямк",
    "id": 4,
    "date_time": "2025-03-01T22:06:40.253000+00:00",
    "limit_people": 0,
    "location": "ыфвмфыфм",
    "description": "фымфымыфк ыфкмыфв",
    "points_for_the_event": 0
  }
]'


## Delete:
Ресурс для удаления мероприятий.


> DELETE '/api/v1/events/delete/{event_id}'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| event_id  | int |



Пример ответа:
'{
  "message": 200
}'


## Базовый ендпоинт: '/visitors/'


## Add:
Ресурс для регистрации пользователя на  мероприятия.


> POST '/api/v1/visitors/add/{event_id}/{user_id}'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| event_id  | int |
| user_id   | int |



Пример ответа:
'{
  "message": 200
}'


## Get:
Ресурс для просмотра мероприятий на которые зарегестрирован пользователь.


> GET '/api/v1/visitors/get/{user_id}'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| user_id   | int |



Пример ответа:
'[
  {
    "event_id": 2,
    "unique_string": "35039281-1eaa-4d75-9951-37c24be4b8ea7b4a9e01-47e9-43a3-b1cb-2cc3421b37f8"
  }
]'


## Delete:
Ресурс для удаления пользователя с мероприятий.


> DELETE '/api/v1/visitors/delete/{event_id}/{user_id}'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| event_id | int |
| user_id  | int |



Пример ответа:
'{
  "message": 200
}'


## Verify:
Ресурс для проверки регистрации пользователя на мероприятии.


> GET '/api/v1/visitors/verify/{unique_string}'


Принимает:


| Name | Type |
|:-------------:|:-------:|
| unique_string  | str |



Пример ответа:
'<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Зарегистрирован</title>
                <style> body { font-family: Arial, Helvetica, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; background-color: #000000; margin: 0; } .message-container { background-color: #018d18; padding: 40px; border-radius: 10px; box-shadow: 0 10px 20px rgb(0, 0, 0); text-align: center; } h1 { font-size: 32px; color: #ffffff; margin-bottom: 20px; } p { font-size: 18px; color: #000000; } </style>
            </head>
            <body>
                <div class="message-container">
                    <h1>Зарегистрирован</h1>
                </div>
            </body>
            </html>'






