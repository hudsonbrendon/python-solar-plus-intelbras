from datetime import datetime, timezone
from unittest.mock import patch

import pytest
from requests_mock import Mocker

from solar_plus_intelbras.enums import KeyEnum, PeriodEnum
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


class TestSolarPlusIntelbrasPlantsDetail:
    def test_should_return_plants_detail(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        plants_detail: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1",
            json=plants_detail,
            status_code=200,
        )
        assert isinstance(solar_plus_intelbras.plants_detail(plant_id=1), dict)
        assert solar_plus_intelbras.plants_detail(plant_id=1) == plants_detail

    def test_shouldnt_return_plants_detail_without_authentication(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        with pytest.raises(Exception):
            solar_plus_intelbras.plants_detail(plant_id=1)

    def test_shouldnt_return_plants_detail_without_plant_id(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        with pytest.raises(Exception):
            solar_plus_intelbras.plants_detail()

    def test_shouldnt_return_plants_detail_string(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        with pytest.raises(Exception):
            solar_plus_intelbras.plants_detail(plant_id="1")

    def test_shouldnt_return_plants_detail_float(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        with pytest.raises(Exception):
            solar_plus_intelbras.plants_detail(plant_id=1.0)


class TestSolarPlusIntelbrasRecords:
    def test_should_return_records_today(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        records_today: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1/records",
            json=records_today,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.records(
                plant_id=1,
                period=PeriodEnum.DAY.value,
                key=KeyEnum.PAC.value,
                start_date="2025-01-23",
                end_date="2025-01-23",
            )
            == records_today
        )

    def test_shouldnt_return_records_with_start_date_invalid(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records(
                plant_id=1,
                period=PeriodEnum.DAY.value,
                key=KeyEnum.PAC.value,
                start_date="2025-01-23",
            )
            assert str(exc.value) == "start_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_records_with_end_date_invalid(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records(
                plant_id=1,
                period=PeriodEnum.DAY.value,
                key=KeyEnum.PAC.value,
                end_date="2025-01-23",
            )
            assert str(exc.value) == "end_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_records_with_start_date_invalid_format(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records(
                plant_id=1,
                period=PeriodEnum.DAY.value,
                key=KeyEnum.PAC.value,
                start_date="2025/01/23",
                end_date="2025-01-23",
            )
            assert str(exc.value) == "start_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_records_with_end_date_invalid_format(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records(
                plant_id=1,
                period=PeriodEnum.DAY.value,
                key=KeyEnum.PAC.value,
                start_date="2025-01-23",
                end_date="2025/01/23",
            )
            assert str(exc.value) == "end_date must be in the format YYYY-MM-DD."


class TestSolarPlusIntelbrasRecordsYear:
    def test_should_return_records_year(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        records_year: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1/records/year?period=year&year=2025&key=energy_today",
            json=records_year,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.records_year(
                year=2025,
                plant_id=1,
            )
            == records_year
        )

    def test_shouldnt_return_records_year_without_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(plant_id=1)
            assert str(exc.value) == "year must be an integer."

    def test_shouldnt_return_records_year_string(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(year="2025", plant_id=1)
            assert str(exc.value) == "year must be an integer."

    def test_shouldnt_return_records_year_float(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(year=2025.0, plant_id=1)
            assert str(exc.value) == "year must be an integer."

    def test_shouldnt_return_records_year_without_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(year=2025)
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_records_year_string_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(year=2025, plant_id="1")
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_records_year_float_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_year(year=2025, plant_id=1.0)
            assert str(exc.value) == "plant_id must be an integer."


class TestSolarPlusIntelbrasRecordsYears:
    def test_should_return_records_years(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        records_years: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1/records/years?start_year=2020&end_year=2025&key=energy_today",
            json=records_years,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.records_years(
                start_year=2020,
                end_year=2025,
                plant_id=1,
            )
            == records_years
        )

    def test_shouldnt_return_records_years_without_start_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(end_year=2025, plant_id=1)
            assert str(exc.value) == "start_year must be an integer."

    def test_shouldnt_return_records_years_string_start_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year="2020", end_year=2025, plant_id=1
            )
            assert str(exc.value) == "start_year must be an integer."

    def test_shouldnt_return_records_years_float_start_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year=2020.0, end_year=2025, plant_id=1
            )
            assert str(exc.value) == "start_year must be an integer."

    def test_shouldnt_return_records_years_without_end_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(start_year=2020, plant_id=1)
            assert str(exc.value) == "end_year must be an integer."

    def test_shouldnt_return_records_years_string_end_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year=2020, end_year="2025", plant_id=1
            )
            assert str(exc.value) == "end_year must be an integer."

    def test_shouldnt_return_records_years_float_end_year(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year=2020, end_year=2025.0, plant_id=1
            )
            assert str(exc.value) == "end_year must be an integer."

    def test_shouldnt_return_records_years_without_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(start_year=2020, end_year=2025)
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_records_years_string_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year=2020, end_year=2025, plant_id="1"
            )
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_records_years_float_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.records_years(
                start_year=2020, end_year=2025, plant_id=1.0
            )
            assert str(exc.value) == "plant_id must be an integer."


class TestSolarPlusIntelbrasInverters:
    def test_should_return_inverters(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        inverters: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1/inverters?limit=20&page=1",
            json=inverters,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.inverters(
                plant_id=1,
                limit=20,
                page=1,
            )
            == inverters
        )

    def test_shouldnt_return_inverters_without_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters()
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_inverters_string_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id="1")
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_inverters_float_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1.0)
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_inverters_without_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1)
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_inverters_string_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1, limit="20")
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_inverters_float_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1, limit=20.0)
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_inverters_without_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1, limit=20)
            assert str(exc.value) == "page must be an integer."

    def test_shouldnt_return_inverters_string_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1, limit=20, page="1")
            assert str(exc.value) == "page must be an integer."

    def test_shouldnt_return_inverters_float_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.inverters(plant_id=1, limit=20, page=1.0)
            assert str(exc.value) == "page must be an integer."


class TestSolarPlusIntelbrasAlerts:
    def test_should_return_alerts(
        self,
        requests_mock: Mocker,
        solar_plus_intelbras: SolarPlusIntelbras,
        alerts: dict,
        login_response: dict,
    ) -> None:
        requests_mock.post(
            "https://ens-server.intelbras.com.br/api/login",
            json=login_response,
            status_code=200,
        )

        requests_mock.get(
            "https://ens-server.intelbras.com.br/api/plants/1/alerts?start_date=2025-01-23&end_date=2025-01-23&limit=20&page=1",
            json=alerts,
            status_code=200,
        )
        assert (
            solar_plus_intelbras.alerts(
                plant_id=1,
                start_date="2025-01-23",
                end_date="2025-01-23",
                limit=20,
                page=1,
            )
            == alerts
        )

    def test_shouldnt_return_alerts_without_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts()
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_alerts_string_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(plant_id="1")
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_alerts_float_plant_id(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(plant_id=1.0)
            assert str(exc.value) == "plant_id must be an integer."

    def test_shouldnt_return_alerts_without_start_date(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(plant_id=1)
            assert str(exc.value) == "start_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_alerts_without_end_date(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(plant_id=1, start_date="2025-01-23")
            assert str(exc.value) == "end_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_alerts_without_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1, start_date="2025-01-23", end_date="2025-01-23"
            )
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_alerts_string_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1, start_date="2025-01-23", end_date="2025-01-23", limit="20"
            )
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_alerts_float_limit(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1, start_date="2025-01-23", end_date="2025-01-23", limit=20.0
            )
            assert str(exc.value) == "limit must be an integer."

    def test_shouldnt_return_alerts_without_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1, start_date="2025-01-23", end_date="2025-01-23", limit=20
            )
            assert str(exc.value) == "page must be an integer."

    def test_shouldnt_return_alerts_string_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1,
                start_date="2025-01-23",
                end_date="2025-01-23",
                limit=20,
                page="1",
            )
            assert str(exc.value) == "page must be an integer."

    def test_shouldnt_return_alerts_float_page(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1,
                start_date="2025-01-23",
                end_date="2025-01-23",
                limit=20,
                page=1.0,
            )
            assert str(exc.value) == "page must be an integer."

    def test_shouldnt_return_alerts_with_start_date_invalid(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1,
                start_date="2025/01/23",
                end_date="2025-01-23",
                limit=20,
                page=1,
            )
            assert str(exc.value) == "start_date must be in the format YYYY-MM-DD."

    def test_shouldnt_return_alerts_with_end_date_invalid(
        self,
        solar_plus_intelbras: SolarPlusIntelbras,
    ) -> None:
        with pytest.raises(Exception) as exc:
            solar_plus_intelbras.alerts(
                plant_id=1,
                start_date="2025-01-23",
                end_date="2025/01/23",
                limit=20,
                page=1,
            )
            assert str(exc.value) == "end_date must be in the format YYYY-MM-DD."
