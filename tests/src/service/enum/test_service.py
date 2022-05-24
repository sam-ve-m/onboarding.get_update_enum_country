from unittest.mock import patch
import pytest

from src.service.enum.service import EnumService
from src.repository.enum.repository import EnumRepository

from tests.test_doubles.doubles import (
    enum_service_get_enums_response_ok,
    enum_service_get_enums_response_invalid,
    enum_service_get_enums_response_none,
)
from tests.test_doubles.doubles import (
    enum_service_response_ok,
    enum_service_response_invalid,
    enum_service_response_none,
)


@patch.object(EnumRepository, "get_enums")
def test_get_response_when_enums_are_ok(get_enums_mock):
    get_enums_mock.return_value = enum_service_get_enums_response_ok
    result = EnumService.get_response()
    assert result == enum_service_response_ok


@patch.object(EnumRepository, "get_enums")
def test_get_response_when_enums_are_none(get_enums_mock):
    get_enums_mock.return_value = enum_service_get_enums_response_none
    result = EnumService.get_response()
    assert result == enum_service_response_none


@patch.object(EnumRepository, "get_enums")
def test_get_response_when_enums_are_invalid(get_enums_mock):
    get_enums_mock.side_effect = Exception("Erroooooou!")
    with pytest.raises(Exception) as error:
        result = EnumService.get_response()
        assert result == enum_service_response_invalid
