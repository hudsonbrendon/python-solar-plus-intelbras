from enum import Enum


class MethodEnum(Enum):
    """A enum with the methods available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class EndpointEnum(Enum):
    """A enum with the endpoints available in the API.

    Args:
        Enum (_type_): A class to represent a enumeration.
    """

    LOGIN = "login"
    PLANTS = "plants"
