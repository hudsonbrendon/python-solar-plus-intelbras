from datetime import datetime, timezone
from unittest.mock import patch

import pytest
from requests_mock import Mocker

from solar_plus_intelbras.solar_plus_intelbras import SolarPlusIntelbras


class TestSolarPlusIntelbras:
    def test_solar_plus_intelbras(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert isinstance(solar_plus_intelbras, SolarPlusIntelbras)

    def test_solar_plus_intelbras_email(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert solar_plus_intelbras.email == "test@email.com"

    def test_solar_plus_intelbras_plus(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert solar_plus_intelbras.plus == "test"

    def test_solar_plus_intelbras_base_api_url(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert (
            solar_plus_intelbras.base_api_url
            == "https://ens-server.intelbras.com.br/api/"
        )

    def test_solar_plus_intelbras_str(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert str(solar_plus_intelbras) == "<SolarPlusIntelbras test@email.com>"

    def test_solar_plus_intelbras_repr(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert repr(solar_plus_intelbras) == "<SolarPlusIntelbras test@email.com>"

    def test_solar_plus_intelbras_token(
        self,
        requests_mock,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.token
            == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InBpY3R1cmUiOiIiLCJpZCI6Njg1MSwiZW1haWwiOiJjb250YXRvLmh1ZHNvbmJyZW5kb25AZ21haWwuY29tIiwibmFtZSI6Ikh1ZHNvbiBCcmVuZG9uIiwiY3BmIjoiIiwicGhvbmUiOiIiLCJjcmVhdGVkQXQiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYxMDY5OC0wMzowMCIsImFjdGl2YXRlZEF0Ijp7IlRpbWUiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYwODEwNS0wMzowMCIsIlZhbGlkIjp0cnVlfSwibGFzdExvZ2luIjoiMjAyNS0wMS0xNyAyMzoyNToxNC4zOTAwMjg0MzYgLTAzMDAgLTAzIG09KzUyMzkyLjQ4ODc5MjE1MSIsInByZWZlcmVuY2VzIjp7ImN1cnJlbmN5IjoiQlJMIiwidGltZXpvbmUiOiItMyIsInRlbXBlcmF0dXJlVW5pdCI6ImMiLCJzZW5kV2VhdGhlck5vdGlmaWNhdGlvbiI6dHJ1ZSwic2VuZEVuZXJneVRvZGF5Tm90aWZpY2F0aW9uIjp0cnVlLCJzZW5kQWxlcnROb3RpZmljYXRpb24iOnRydWV9LCJyZWdpc3RyYXRpb25Ub2tlbiI6ImQxbWNVRzNVSjA5UHN3d0JDLXVFUDk6QVBBOTFiRzJ4Z3dXUDIzVFhab0tiejVIamZpQW9EbnIxeGEtT1haVTZDMXVEQWIyczZPU3NkRHdMQ3VYTWxkdnBYM0ZJcF9jQloxRU4zU2xsZm5nWmVCYU1aNUNsLWhvcGNLajNhWnRWTTE0MEsyT1U4Tno3eHMiLCJhY3RpdmF0aW9uQ29kZSI6ImU2YjE2OGRkZjc0M2QwOWE4OGU2NmYwZWZhMDZiMDE1In0sImV4cCI6MTczNzE3NTcxNiwiaWF0IjoxNzM3MTc1NDE2LCJjb2RlIjoiIiwicm9sZSI6ImNsaWVudCJ9.FXOp76WgRRemmiOr2z4ML6QVEG1fbDYk1LfYK_hm3vs"
        )

    def test_solar_plus_intelbras_login(
        self,
        requests_mock,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        assert solar_plus_intelbras._login() == login_response

    def test_solar_plus_intelbras_token_error(
        self,
        requests_mock,
        login_response: dict,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        login_response.pop("accessToken")
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        with pytest.raises(KeyError):
            solar_plus_intelbras.token

    def test_should_return_true_solar_plus_intelbras_is_token_not_defined(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert solar_plus_intelbras._is_token_expired() is True

    @pytest.mark.freeze_time("2025-01-01 00:00:00")
    def test_should_return_true_solar_plus_intelbras_is_token_and_datetime_now_equals(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
    ) -> None:
        login_response["accessToken"]["exp"] = int(
            datetime.now(timezone.utc).timestamp()
        )
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        solar_plus_intelbras._login()
        assert solar_plus_intelbras._is_token_expired() is True

    @pytest.mark.freeze_time("2025-01-01 00:00:00")
    def test_should_return_true_solar_plus_intelbras_is_token_expired(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
    ) -> None:
        login_response["accessToken"]["exp"] = int(
            datetime.now(timezone.utc).timestamp() - 1
        )
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        solar_plus_intelbras._login()
        assert solar_plus_intelbras._is_token_expired() is True

    @pytest.mark.freeze_time("2025-01-01 00:00:00")
    def test_should_return_false_solar_plus_intelbras_is_token_not_expired(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
    ) -> None:
        login_response["accessToken"]["exp"] = int(
            datetime.now(timezone.utc).timestamp() + 1
        )
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        solar_plus_intelbras._login()
        assert solar_plus_intelbras._is_token_expired() is False

    def test_token_expired(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with patch.object(
            solar_plus_intelbras, "_is_token_expired"
        ) as mock_is_token_expired:
            mock_is_token_expired.return_value = True
            with patch.object(solar_plus_intelbras, "_login") as mock_login:
                solar_plus_intelbras.token
                mock_login.assert_called_once()

    @pytest.mark.freeze_time("2025-01-01 00:00:00")
    def test_login_without_exp(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
        login_response: dict,
        requests_mock: Mocker,
    ) -> None:
        login_response["accessToken"].pop("exp")
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )
        solar_plus_intelbras._login()
        assert solar_plus_intelbras._token_expiration == datetime.now(timezone.utc)


class TestSolarPlusIntelbrasPlants:
    def test_should_return_plants(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        plants: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants",
            json=plants,
            status_code=200,
        )
        assert isinstance(solar_plus_intelbras.plants(), dict)
        assert solar_plus_intelbras.plants() == plants

    def test_shouldnt_return_plants_without_authentication(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        with pytest.raises(Exception):
            solar_plus_intelbras.plants()
