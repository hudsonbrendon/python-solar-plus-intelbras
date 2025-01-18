from solar_plus_intelbras.enums import EndpointEnum, MethodEnum
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

    def test_solar_plus_intelbras_request(
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
            solar_plus_intelbras._request(
                method=MethodEnum.POST, endpoint=EndpointEnum.LOGIN
            )
            == login_response
        )
