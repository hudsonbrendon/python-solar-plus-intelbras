from enum import Enum


class EndpointEnum(Enum):
    """A enum with the endpoints available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    LOGIN = "login"
    PLANTS = "plants"
    RECORDS = "records"


class PeriodEnum(Enum):
    """A enum with the periods available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    DAY = "day"
    MONTH = "month"
    YEAR = "year"
