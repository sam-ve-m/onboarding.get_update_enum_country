from unittest.mock import patch

from main import get_enums
from src.repository.country_enum.repository import CountryEnumRepository
from src.service.country_enum.service import CountryEnumService
from tests.test_doubles.doubles import main_service_response_dummy, main_response_dummy, \
    enum_service_get_enums_response_none, enum_service_response_none, enum_service_response_invalid

service_response_dummy = main_service_response_dummy


@patch.object(CountryEnumService, "get_response")
def test_response_when_is_all_ok(get_response_mock):
    get_response_mock.return_value = service_response_dummy
    response = get_enums()
    expected_response = main_response_dummy
    assert response.data == expected_response


@patch.object(CountryEnumRepository, "get_country_enum")
def test_get_response_when_enums_are_none(get_enums_mock):
    get_enums_mock.return_value = enum_service_get_enums_response_none
    result = get_enums()
    assert result.data == enum_service_response_none.encode()


@patch.object(CountryEnumRepository, "get_country_enum")
def test_get_response_when_enums_are_invalid(get_enums_mock):
    get_enums_mock.side_effect = Exception("Erroooooou!")
    result = get_enums()
    assert result.data == enum_service_response_invalid.encode()
