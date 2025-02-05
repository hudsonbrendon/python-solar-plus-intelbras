from decouple import config

from solar_plus_intelbras import SolarPlusIntelbras

solar_plus_intelbras = SolarPlusIntelbras(
    email=config("SOLAR_PLUS_EMAIL"),
    plus=config("SOLAR_PLUS_PLUS"),
)


if __name__ == "__main__":
    print(
        solar_plus_intelbras.records_years(
            start_year=2024, end_year=2025, plant_id=config("SOLAR_PLUS_PLANT_ID")
        )
    )
