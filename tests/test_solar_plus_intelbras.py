import pytest

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
