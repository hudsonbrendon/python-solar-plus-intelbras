from decouple import config

from solar_plus_intelbras import SolarPlusIntelbras

solar_plus_intelbras = SolarPlusIntelbras(
    email=config("SOLAR_PLUS_EMAIL"),
    plus=config("SOLAR_PLUS_PLUS"),
)


if __name__ == "__main__":
    print(solar_plus_intelbras.inverters(plant_id=config("SOLAR_PLUS_PLANT_ID")))
