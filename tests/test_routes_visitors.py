from unittest.mock import AsyncMock, patch

from pytest import mark

from .constant import PATH_VISITOR, TEST_GET_VISITOR_EVENTS
from .requests import UserEventSchema, UserSchema


@mark.parametrize(
    ("event_id", "user_id", "code"),
    [
        (1, "4c295c15-1b0d-41ae-b36b-92c9ca423494", 201),
        (2, "e83e8ac6-7609-45d0-ae56-c6fe8f03c4da", 201),
    ],
)
def test_route_add_visitor_ok(client, event_id, user_id, code):
    with patch("src.controllers.VisitorsControl.create_user", new_callable=AsyncMock):
        response = client.post(url=f"{PATH_VISITOR}add/{event_id}/{user_id}")

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [([], 404), ({}, 404), (None, 404)],
)
def test_route_add_visitor_bad(client, payload, code):
    with patch("src.controllers.VisitorsControl.create_user", new_callable=AsyncMock):
        response = client.post(url=f"{PATH_VISITOR}add", json=payload)

        assert response.status_code == code


@mark.parametrize(
    ("user_id", "code"),
    [
        ("4c295c15-1b0d-41ae-b36b-92c9ca423494", 200),
        ("e83e8ac6-7609-45d0-ae56-c6fe8f03c4da", 200),
    ],
)
def test_route_get_visitor_ok(client, user_id, code):
    with patch("src.controllers.VisitorsControl.get_user_events", new_callable=AsyncMock) as mock:
        mock.return_value = UserEventSchema(
            user_event=[UserSchema(**events) for events in TEST_GET_VISITOR_EVENTS]
        )
        response = client.get(url=f"{PATH_VISITOR}get/{user_id}")

        assert response.status_code == code


@mark.parametrize(
    ("user_id", "code"),
    [([], 422), ({}, 422), (None, 422)],
)
def test_route_get_visitor_bad(client, user_id, code):
    with patch("src.controllers.VisitorsControl.get_user_events", new_callable=AsyncMock) as mock:
        mock.return_value = UserEventSchema(
            user_event=[UserSchema(**events) for events in TEST_GET_VISITOR_EVENTS]
        )
        response = client.get(url=f"{PATH_VISITOR}get/{user_id}")

        assert response.status_code == code


@mark.parametrize(
    ("event_id", "user_id", "code"),
    [
        (1, "4c295c15-1b0d-41ae-b36b-92c9ca423494", 204),
        (2, "e83e8ac6-7609-45d0-ae56-c6fe8f03c4da", 204),
    ],
)
def test_route_delete_visitors_ok(client, event_id, user_id, code):
    with patch("src.controllers.VisitorsControl.delete_user", new_callable=AsyncMock):
        response = client.delete(url=f"{PATH_VISITOR}delete/{event_id}/{user_id}")

        assert response.status_code == code


@mark.parametrize(
    ("event_id", "user_id", "code"),
    [("1", None, 422), ({}, "22", 422), (None, {}, 422)],
)
def test_route_delete_visitors_bad(client, event_id, user_id, code):
    with patch("src.controllers.VisitorsControl.delete_user", new_callable=AsyncMock):
        response = client.delete(url=f"{PATH_VISITOR}delete/{event_id}/{user_id}")

        assert response.status_code == code
