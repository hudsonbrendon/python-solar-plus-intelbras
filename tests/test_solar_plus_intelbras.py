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

    def test_solar_plus_intelbras_str(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert str(solar_plus_intelbras) == "<SolarPlusIntelbras test@email.com>"

    def test_solar_plus_intelbras_repr(
        self, solar_plus_intelbras: SolarPlusIntelbras
    ) -> None:
        assert repr(solar_plus_intelbras) == "<SolarPlusIntelbras test@email.com>"
