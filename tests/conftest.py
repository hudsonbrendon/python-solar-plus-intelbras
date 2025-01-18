import pytest

from solar_plus_intelbras.solar_plus_intelbras import SolarPlusIntelbras


@pytest.fixture
def solar_plus_intelbras() -> SolarPlusIntelbras:
    return SolarPlusIntelbras("test@email.com", "test")
