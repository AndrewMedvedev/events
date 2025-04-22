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
| points_for_the_event | int or None |
| limit_people | int or None |

## Примеры ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 201

Отрицательные:
  Неправильно заполнен json -> status_code: 422
  Некоректные значения -> status_code: 400
  Такие данные уже существуют -> status_code: 409


## Get:
Ресурс для просмотра всех  мероприятий с возможностью получать данные по страницам.

> GET '/api/v1/events/get/'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| is_paginated | bool |
| page | int |
| limit | int |
 
## Пример ответа:
"Если флаг is_paginated == False то придут все мероприятия, is_paginated == True то придут по страницам, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  is_paginated: False
  status_code: 200
  body: 
    "events: {[
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
    ]},"

  is_paginated: True
  page: 1
  limit: 3
  status_code: 200
  body: 
    'events: {[
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
      }
    ]}'

Отрицательные:
  Неправильно заполнены поля -> status_code: 422


## Delete:
Ресурс для удаления мероприятий.

> DELETE '/api/v1/events/delete/{event_id}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| event_id  | int |

## Примеры ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 204

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Попытка удаления несуществующей записи -> status_code: 400


## Базовый ендпоинт: '/news/'


## Add:
Ресурс для создания новости.

> POST '/api/v1/news/add/'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| title  | str |
| body   | str |
| image   | bytes | None |

## Пример ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 201

Отрицательные:
  Неправильно заполненные поля -> status_code: 422
  Такие данные уже существуют -> status_code: 409
  Некоректные значения -> status_code: 400


## Get:
Ресурс для просмотра всех новостей с возможностью получать данные по страницам.

> GET "/api/v1/news/get/"

Принимает:

| Name | Type |
|:-------------:|:-------:|
| is_paginated | bool |
| page | int |
| limit | int |

## Пример ответа:
"Если флаг is_paginated == False то придут все новости без изображения, придет только путь по которому хранится изображение, is_paginated == True то придут по страницам, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  is_paginated: False
  page: 1
  limit: 10
  status_code: 200
  body:
      "{news: [
    {
        "id": 1,
        "title": "adsbfdbdafb",
        "body": "fbadfbadfbdafb",
        "image": "images\\eda3b219-fbdc-4a02-bd41.jpg",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 2,
        "title": "dafbdfb",
        "body": "fbadfbadfbdafb",
        "image": "images\\eda3b219-fbdc-524a9547f41.jpg",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 3,
        "title": "dsfbdfab",
        "body": "fbadfbadfbdafb",
        "image": "images\\e-fbdc-4a02-bd77-c524a9547f41.jpg",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 4,
        "title": "dfbgdfsbfd",
        "body": "fbadfbadfbdafb",
        "image": "images\\ed-fbdc-4a02-bd77-c524a9547f41.jpg",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 5,
        "title": "adfbdf",
        "body": "fbadfbadfbdafb",
        "image": "images\\eda3b219-fbdc-4a-c524a9547f41.jpg",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    ] 
      }"

  is_paginated: True
  page: 1
  limit: 3
  status_code: 200
  body:
      "{news: [
    {
        "id": 1,
        "title": "adsbfdbdafb",
        "body": "fbadfbadfbdafb",
        "image": "какое то изображение в виде строки base64",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 2,
        "title": "dafbdfb",
        "body": "fbadfbadfbdafb",
        "image": "какое то изображение в виде строки base64",
        "created_at": "2025-04-17T18:49:58.050080",
    },
    {
        "id": 3,
        "title": "dsfbdfab",
        "body": "fbadfbadfbdafb",
        "image": "какое то изображение в виде строки base64",
        "created_at": "2025-04-17T18:49:58.050080",
    }
    ] 
      }"

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Некоректные значения -> status_code: 400


## Delete:
Ресурс для удаления мероприятий.

> DELETE '/api/v1/news/delete/{news_id}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| news_id  | int |

## Примеры ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 204

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Попытка удаления несуществующей записи -> status_code: 400


## Базовый ендпоинт: '/visitors/'


## Add:
Ресурс для регистрации пользователя на  мероприятия.

> POST '/api/v1/visitors/add/{event_id}/{user_id}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| event_id  | int |
| user_id   | int |

## Пример ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 201

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Такие данные уже существуют -> status_code: 409
  Некоректные значения -> status_code: 400
  Попытка зарегестрировать несуществующего пользователя: -> status_code: 400
  Попытка зарегестрироваться на несуществующее мероприятие: -> status_code: 400


## Get:
Ресурс для просмотра мероприятий на которые зарегестрирован пользователь.

> GET '/api/v1/visitors/get/{user_id}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| user_id   | int |


## Пример ответа:
"При правильном заполнении вернутся мероприятие и уникальная строка на которые зарегестрирован пользователь, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 200
  body: 
    'user_event: {[
      {
        "event_id": 2,
        "unique_string": "35039281-1eaa-4d75-9951-37c24be4b8ea7b4a9e01-47e9-43a3-b1cb-2cc3421b37f8"
      }
    ]}'

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Попытка получить мероприятия несуществующего пользователя: -> status_code: 400


## Delete:
Ресурс для удаления пользователя с мероприятий.

> DELETE '/api/v1/visitors/delete/{event_id}/{user_id}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| event_id | int |
| user_id  | int |

## Примеры ответа:
"При правильном заполненении приходит только статус код, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:
  status_code: 204

Отрицательные:
  Неправильно заполненно поле -> status_code: 422
  Попытка удаления несуществующей записи -> status_code: 400


## Verify:
Ресурс для проверки регистрации пользователя на мероприятии.

> GET '/api/v1/visitors/verify/{unique_string}'

Принимает:

| Name | Type |
|:-------------:|:-------:|
| unique_string  | str |

## Пример ответа:
"При правильном заполненении приходит HTML страницы, при возникновении ошибки возвращается статус код и тело вида: {
            "message": self.message,
            "description": self.description,
            "error": f"{type(self.error)} - {self.error}",
        }"

Положительные:

  status_code: 200
  body:
    '<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Зарегистрирован</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #000000 0%, #24a304 100%);
            font-family: 'Arial', sans-serif;
        }

        .registration-banner {
            width: 100%;
            max-width: 400px;
            text-align: center;
            color: #ffffff;
        }

        .banner-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 25px;
        }

        .user-info {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(21, 252, 0, 0.05);
        }

        .info-row {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            margin: 10px 0;
            border-bottom: 1px solid #eee;
        }

        .info-row:last-child {
            border-bottom: none;
        }

        .info-label {
            font-weight: bold;
            color: #000000;
        }

        .info-value {
            color: #000000;
        }
    </style>
</head>
<body>
<div class="registration-banner">
    <div class="banner-title">Зарегистрирован</div>
    <div class="user-info">
        <div class="info-row">
            <span class="info-label">Имя:</span>
            <span class="info-value">{{ first_name }}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Фамилия:</span>
            <span class="info-value">{{ last_name }}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Email:</span>
            <span class="info-value">{{ email }}</span>
        </div>
    </div>
</div>
</body>
</html>'

Отрицательные:
  Неправильно заполненно поле(тип поля) -> status_code: 422
  Неверная строка -> 
  status_code: 200
  body: 
    "<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Не Зарегистрирован</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #000000;
            margin: 0;
        }
        .message-container {
            background-color: #b30606;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgb(0, 0, 0);
            text-align: center;
        }
        h1 {
           font-size: 32px;
           color: #ffffff;
           margin-bottom: 20px;
        }
        p {
           font-size: 18px; color: #000000;
        }
    </style>
</head>
<body>
    <div class="message-container">
        <h1>Не Зарегистрирован</h1>
    </div>
</body>
</html>"




