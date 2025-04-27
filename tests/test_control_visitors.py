from unittest.mock import MagicMock

from fastapi import Request
from pytest import mark, raises

from src.exeptions import BadRequestHTTPError
from tests.constant import (
    LEN_GET_VISITOR_EVENTS,
    TEST_GET_VISITOR_EVENTS,
    TEST_VERIFY_VISITOR,
)

from .requests import UserEventSchema, UserSchema


@mark.parametrize(
    ("event_id", "user_id"),
    [
        (1, "4c295c15-1b0d-41ae-b36b-92c9ca423494"),
        (2, "e83e8ac6-7609-45d0-ae56-c6fe8f03c4da"),
    ],
)
def test_control_create_user_ok(visitor_mock, event_id, user_id):
    visitor_mock.create_event.return_value = None
    result = visitor_mock.create_event(event_id, user_id)
    assert result is None


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [([],), ({},), (None,)],
)
async def test_control_create_user_bad(visitor_mock, payload):
    visitor_mock.create_event.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await visitor_mock.create_event(payload)


@mark.asyncio
@mark.parametrize(
    ("user_id"),
    [
        ("4c295c15-1b0d-41ae-b36b-92c9ca423494",),
        ("e83e8ac6-7609-45d0-ae56-c6fe8f03c4da",),
    ],
)
async def test_control_get_visitor_ok(visitor_mock, user_id):
    visitor_mock.get_user_events.return_value = UserEventSchema(
        user_event=[UserSchema(**events) for events in TEST_GET_VISITOR_EVENTS]
    )
    result = await visitor_mock.get_user_events(user_id)

    assert len(result.user_event) == LEN_GET_VISITOR_EVENTS


@mark.asyncio
@mark.parametrize(
    ("user_id"),
    [([],), ({},), (None,)],
)
async def test_control_get_visitor_bad(visitor_mock, user_id):
    visitor_mock.get_user_events.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await visitor_mock.get_user_events(user_id)


@mark.parametrize(
    ("event_id", "user_id"),
    [
        (1, "4c295c15-1b0d-41ae-b36b-92c9ca423494"),
        (2, "e83e8ac6-7609-45d0-ae56-c6fe8f03c4da"),
    ],
)
def test_control_delete_visitors_ok(visitor_mock, event_id, user_id):
    visitor_mock.delete_user.return_value = None
    result = visitor_mock.delete_user(event_id, user_id)
    assert result is None


@mark.asyncio
@mark.parametrize(
    ("event_id", "user_id"),
    [
        (1, "4c295c15-1b0d-41ae-b36b-92c9ca423494"),
        (2, "e83e8ac6-7609-45d0-ae56-c6fe8f03c4da"),
    ],
)
async def test_control_delete_visitors_bad(visitor_mock, event_id, user_id):
    visitor_mock.delete_user.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await visitor_mock.delete_user(event_id, user_id)


@mark.parametrize(
    ("unique_string"),
    [("kjsndvkj sjk dvs ivbhsiuvs"), ("hjbvjbuew  76478263872 uehwi fgeuig fqoiu")],
)
def test_control_verify_visitor_ok(visitor_mock, unique_string):
    visitor_mock.verify.return_value = TEST_VERIFY_VISITOR
    result = visitor_mock.verify(MagicMock(spec=Request), unique_string)

    assert result["request"] == "req"


@mark.parametrize(
    ("unique_string"),
    [("kjsdavadsdvas235423542"), ("bsj bvdsabvbsbduvs nigga iweufiwhi")],
)
def test_control_verify_visitor_bad(visitor_mock, unique_string):
    visitor_mock.verify.return_value = None
    result = visitor_mock.verify(MagicMock(spec=Request), unique_string)

    assert result is None
