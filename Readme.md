# Документация REST API

## Сервис мероприятий

## Базовый ендпоинт: '/events/'

## Add

Ресурс для создания мероприятий.

> POST '/api/v1/events/'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| id | int | автозаполняемый |
| name_event | str | обязательное заполнение |
| date_time | datetime | автозаполняемый |
| location | str | обязательное заполнение |
| description | str | обязательное заполнение |
| points_for_the_event | int | не обязательное заполнение |
| limit_people | int  | обязательное заполнение |

## Примеры ответа

<b>Response</b>

- **201 Created**

```json
{
  "title": "EventSchema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "ID события",
      "nullable": true
    },
    "name_event": {
      "type": "string",
      "description": "Название события"
    },
    "date_time": {
      "type": "string",
      "format": "date-time",
      "description": "Дата и время события"
    },
    "location": {
      "type": "string",
      "description": "Местоположение"
    },
    "description": {
      "type": "string",
      "description": "Описание события"
    },
    "points_for_the_event": {
      "type": "number",
      "format": "float",
      "default": 0,
      "description": "Баллы за событие"
    },
    "limit_people": {
      "type": "integer",
      "default": 0,
      "description": "Лимит участников"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Дата создания записи"
    }
  },
}
```

## Get

Ресурс для просмотра всех  мероприятий с возможностью получать данные по страницам.

> GET '/api/v1/events/'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| page | int | не обязательное заполнение |
| limit | int | не обязательное заполнение |

<b>Response</b>

- **200 OK**

```json
list[{
  "title": "EventSchema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "ID события",
      "nullable": true
    },
    "name_event": {
      "type": "string",
      "description": "Название события"
    },
    "date_time": {
      "type": "string",
      "format": "date-time",
      "description": "Дата и время события"
    },
    "location": {
      "type": "string",
      "description": "Местоположение"
    },
    "description": {
      "type": "string",
      "description": "Описание события"
    },
    "points_for_the_event": {
      "type": "number",
      "format": "float",
      "default": 0,
      "description": "Баллы за событие"
    },
    "limit_people": {
      "type": "integer",
      "default": 0,
      "description": "Лимит участников"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Дата создания записи"
    }
  },
}]
```

## Delete

Ресурс для удаления мероприятий.

> DELETE '/api/v1/events/{event_id}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| event_id  | int | обязательное заполнение |

<b>Response</b>

- **204 No content**

```json
{
  "None"
}
```

## Базовый ендпоинт: '/news/'

## Add

Ресурс для создания новости.

> POST '/api/v1/news/'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| title  | str | обязательное заполнение |
| body   | str | обязательное заполнение |
| image   | bytes | не обязательное заполнение |

<b>Response</b>

- **201 Created**

```json
{
  "title": "NewsSchema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "ID новости",
      "nullable": true
    },
    "title": {
      "type": "string",
      "description": "Заголовок новости"
    },
    "body": {
      "type": "string",
      "description": "Текст новости"
    },
    "image": {
      "type": "string(base64)",
      "description": "Изображение новости",
      "nullable": true
    }
  },
}
```

## Get

Ресурс для просмотра всех новостей с возможностью получать данные по страницам.

> GET "/api/v1/news/"

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| page | int | не обязательное заполнение |
| limit | int | не обязательное заполнение |

<b>Response</b>

- **200 OK**

```json
list[{
  "title": "NewsSchema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "ID новости",
      "nullable": true
    },
    "title": {
      "type": "string",
      "description": "Заголовок новости"
    },
    "body": {
      "type": "string",
      "description": "Текст новости"
    },
    "image": {
      "type": "string(base64)",
      "description": "Изображение новости",
      "nullable": true
    }
  },
}]
```

## Delete

Ресурс для удаления мероприятий.

> DELETE '/api/v1/news/{news_id}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| news_id  | int | обязательное заполнение |

<b>Response</b>

- **204 No content**

```json
{
  "None"
}
```

## Базовый ендпоинт: '/visitors/'

## Add

Ресурс для регистрации пользователя на  мероприятия.

> POST '/api/v1/visitors/{event_id}/{user_id}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| event_id | int | обязательное заполнение |
| user_id | uuid4 | обязательное заполнение |

<b>Response</b>

- **201 Created**

```json
{
  "None"
}
```

## Get

Ресурс для просмотра мероприятий на которые зарегестрирован пользователь.

> GET '/api/v1/visitors/{user_id}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| user_id | uuid4 | обязательное заполнение |

<b>Response</b>

- **200 OK**

```json
list[{
  "id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "first_name": "Иван",
  "last_name": "Петров",
  "email": "ivan.petrov@example.com",
  "event_id": 5,
  "unique_string": "550e8400-e29b-41d4-a716-446655440000550e8400-e29b-41d4-a716-446655440001",
  "created_at": "2024-01-15T14:30:00Z"
}]
```

## Delete

Ресурс для удаления пользователя с мероприятий.

> DELETE '/api/v1/visitors/{event_id}/{user_id}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| user_id | uuid | обязательное заполнение |
| event_id | int | обязательное заполнение |

<b>Response</b>

- **204 No content**

```json
{
  "None"
}
```

## Verify

Ресурс для проверки регистрации пользователя на мероприятии.

> GET '/api/v1/visitors/verify/{unique_string}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| unique_string  | str | обязательное заполнение |

<b>Response</b>

- **200 OK**

```html
<!DOCTYPE html>
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
</html>
```

<b>Response</b>

- **200 OK**

```html
<!DOCTYPE html>
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
</html>
```

## Make QR

Ресурс для создания qr кода.

> GET '/api/v1/visitors/make/qr/{unique_string}'

Принимает:

| Name | Type | Filling |
|:-------------:|:-------------:|:-------------:|
| unique_string  | str | обязательное заполнение |

<b>Response</b>

- **200 OK**

```json
{
  "Файл с qr кодом"
}
```
