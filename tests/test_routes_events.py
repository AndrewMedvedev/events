from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

from pytest import mark

from .constant import PATH_EVENT, TEST_GET_ALL_EVENTS, TEST_GET_WITH_LIMIT_EVENTS
from .requests import EventGetParams, EventListResponse, EventResponse, EventSchema


@mark.parametrize(
    ("payload", "code"),
    [
        (
            EventSchema(
                name_event="name",
                date_time=datetime.now(tz=UTC),
                location="street",
                description="description",
            ),
            201,
        ),
        (
            EventSchema(
                name_event="names",
                date_time=(datetime.now(tz=UTC)),
                location="streets",
                description="descriptions",
                points_for_the_event=11,
                limit_people=411,
            ),
            201,
        ),
    ],
)
def test_route_add_event_ok(client, payload, code):
    with patch("src.controllers.EventControl.create_event", new_callable=AsyncMock):
        response = client.post(url=f"{PATH_EVENT}add", json=payload.to_dict())

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [([], 422), ({}, 422), (None, 422)],
)
def test_route_add_event_bad(client, payload, code):
    with patch("src.controllers.EventControl.create_event", new_callable=AsyncMock):
        response = client.post(url=f"{PATH_EVENT}add", json=payload)

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [
        (EventGetParams(is_paginated=False, page=1, limit=10), 200),
        (EventGetParams(is_paginated=True, page=1, limit=10), 200),
    ],
)
def test_route_get_events_ok(client, payload, code):
    with patch("src.controllers.EventControl.get_event", new_callable=AsyncMock) as mock:
        test_data = TEST_GET_ALL_EVENTS
        if payload.is_paginated is True:
            test_data = TEST_GET_WITH_LIMIT_EVENTS
        mock.return_value = EventListResponse(
            events=[EventResponse(**event) for event in test_data]
        )

        response = client.get(url=f"{PATH_EVENT}get", params=payload.to_dict())

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [({"is_paginated": ""}, 422), ({"page": ""}, 422), ({"limit": ""}, 422)],
)
def test_route_get_events_bad(client, payload, code):
    with patch("src.controllers.EventControl.get_event", new_callable=AsyncMock) as mock:
        mock.return_value = EventListResponse(
            events=[EventResponse(**event) for event in TEST_GET_ALL_EVENTS]
        )

        response = client.get(url=f"{PATH_EVENT}get", params=payload)

        assert response.status_code == code


@mark.parametrize(
    ("event_id", "code"),
    [
        (1, 204),
        (2, 204),
    ],
)
def test_route_delete_events_ok(client, event_id, code):
    with patch("src.controllers.EventControl.delete_event", new_callable=AsyncMock):
        response = client.delete(url=f"{PATH_EVENT}delete/{event_id}")

        assert response.status_code == code


@mark.parametrize(
    ("event_id", "code"),
    [([], 422), ({}, 422), (None, 422)],
)
def test_route_delete_events_bad(client, event_id, code):
    with patch("src.controllers.EventControl.delete_event", new_callable=AsyncMock):
        response = client.delete(url=f"{PATH_EVENT}delete/{event_id}")

        assert response.status_code == code
