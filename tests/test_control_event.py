from datetime import UTC, datetime

from pytest import mark, raises

from src.exeptions import BadRequestHTTPError

from .constant import (
    LEN_GET_ALL_EVENTS,
    LEN_GET_WITH_LIMIT_EVENTS,
    TEST_GET_ALL_EVENTS,
    TEST_GET_WITH_LIMIT_EVENTS,
)
from .requests import EventGetParams, EventListResponse, EventResponse, EventSchema


@mark.parametrize(
    ("payload"),
    [
        (
            EventSchema(
                name_event="name",
                date_time=datetime.now(tz=UTC),
                location="street",
                description="description",
            ),
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
        ),
    ],
)
def test_control_create_events_ok(event_mock, payload):
    event_mock.create_event.return_value = None
    result = event_mock.create_event(payload)
    assert result is None


@mark.asyncio
@mark.parametrize(
    "payload",
    [
        "invalid_string",
        {"invalid": "data"},
        None,
    ],
)
async def test_control_create_events_bad(event_mock, payload):
    event_mock.create_event.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await event_mock.create_event(payload)


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [
        (EventGetParams(is_paginated=False, page=1, limit=10)),
        (EventGetParams(is_paginated=True, page=1, limit=10)),
    ],
)
async def test_control_get_events_ok(event_mock, payload):
    test_data = TEST_GET_ALL_EVENTS
    result_data = LEN_GET_ALL_EVENTS
    if payload.is_paginated is not False:
        test_data = TEST_GET_WITH_LIMIT_EVENTS
        result_data = LEN_GET_WITH_LIMIT_EVENTS
    event_mock.get_event.return_value = EventListResponse(
        events=[EventResponse(**event) for event in test_data]
    )
    result = await event_mock.get_event(payload)

    assert len(result.events) == result_data


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [({"is_paginated": ""}), ({"page": ""}), ({"limit": ""})],
)
async def test_control_get_events_bad(event_mock, payload):
    event_mock.get_event.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await event_mock.get_event(payload)


@mark.parametrize(
    ("event_id"),
    [
        (1),
        (2),
    ],
)
def test_control_delete_events_ok(event_mock, event_id):
    event_mock.delete_event.return_value = None
    result = event_mock.delete_event(event_id)
    assert result is None


@mark.asyncio
@mark.parametrize(
    ("event_id"),
    [([]), ({}), (None)],
)
async def test_control_delete_events_bad(event_mock, event_id):
    event_mock.delete_event.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await event_mock.delete_event(event_id)
