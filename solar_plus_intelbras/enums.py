from enum import Enum


class EndpointEnum(Enum):
    """A enum with the endpoints available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    LOGIN = "login"
    PLANTS = "plants"
    RECORDS = "records"
    RECORDS_YEAR = "records/year"
    RECORDS_YEARS = "records/years"
    INVERTERS = "inverters"
    USER = "user"
    NOTIFICATIONS = "notifications"


class PeriodEnum(Enum):
    """A enum with the periods available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    DAY = "day"
    MONTH = "month"
    YEAR = "year"


class KeyEnum(Enum):
    """A enum with the keys available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    PAC = "pac"
    ENERGY_TODAY = "energy_today"
