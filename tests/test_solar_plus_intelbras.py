from solar_plus_intelbras.solar_plus_intelbras import SolarPlusIntelbras


class TestSolarPlusIntelbras:
    def test_solar_plus_intelbras(self):
        instance = SolarPlusIntelbras()

        assert isinstance(instance, SolarPlusIntelbras)
