from enum import Enum


class EndpointEnum(Enum):
    """Enum with the available endpoints for the Intelbras API."""

    LOGIN = "login"
    PLANTS = "plants"
