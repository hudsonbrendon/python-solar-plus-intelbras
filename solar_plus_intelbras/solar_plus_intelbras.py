import requests
from pydantic import EmailStr

from solar_plus_intelbras.enums import EndpointEnum, MethodEnum


class SolarPlusIntelbras:
    """A class to represent a SolarPlusIntelbras.

    Returns:
        _type_: SolarPlusIntelbras
    """

    __BASE_API_URL = "https://ens-server.intelbras.com.br/api/"

    def __init__(self, email: EmailStr, plus: str) -> None:
        """Construct a SolarPlusIntelbras object.

        Args:
            email (EmailStr): A valid email address.
            plus (str): A string.
        """
        self.__email = email
        self.__plus = plus

    @property
    def email(self) -> EmailStr:
        """Return the email attribute.

        Returns:
            EmailStr: A valid email address.
        """
        return self.__email

    @property
    def plus(self) -> str:
        """Return the plus attribute.

        Returns:
            str: A string.
        """
        return self.__plus

    @property
    def base_api_url(self) -> str:
        """Return the base_api_url attribute.

        Returns:
            str: A string.
        """
        return self.__BASE_API_URL

    def __str__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string.
        """
        return f"<SolarPlusIntelbras {self.email}>"

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string.
        """
        return self.__str__()

    def _request(self, method: MethodEnum, endpoint: EndpointEnum) -> dict:
        """A private method to make a request to the API.

        Args:
            method (MethodEnum): A method from the MethodEnum.
            endpoint (EndpointEnum): A endpoint from the EndpointEnum.

        Returns:
            dict: A response from the API.
        """
        response = requests.request(
            method.value, f"{self.base_api_url}{endpoint.value}"
        )
        response.raise_for_status()
        return response.json()
