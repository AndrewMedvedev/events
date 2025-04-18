from pytest import mark

from src.schemas import EventListResponse, EventResponse

from .constant import (
    LEN_GET_ALL_EVENTS,
    LEN_GET_WITH_LIMIT_EVENTS,
    TEST_GET_ALL_EVENTS,
    TEST_GET_WITH_LIMIT_EVENTS,
)

pytestmark = [
    mark.asyncio,
]


async def test_get_all_events(event_mock):
    event_mock.get_event.return_value = EventListResponse(
            events=[EventResponse(**event) for event in TEST_GET_ALL_EVENTS]
        )
    result = await event_mock.get_event(
        is_paginated=False,
        page=1,
        limit=10
    )

    assert len(result.events) == LEN_GET_ALL_EVENTS


async def test_get_events_with_limit(event_mock):
    event_mock.get_event.return_value = EventListResponse(
            events=[EventResponse(**event) for event in TEST_GET_WITH_LIMIT_EVENTS]
        )
    result = await event_mock.get_event(is_paginated=True, page=1, limit=4)

    assert len(result.events) == LEN_GET_WITH_LIMIT_EVENTS
