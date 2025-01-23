from datetime import datetime, timezone

import requests
from pydantic import EmailStr

from solar_plus_intelbras.enums import EndpointEnum


class SolarPlusIntelbras:
    """A class to represent a SolarPlusIntelbras."""

    __BASE_API_URL = "https://ens-server.intelbras.com.br/api/"

    def __init__(self, email: EmailStr, plus: str) -> None:
        """Construct a SolarPlusIntelbras object.

        Args:
            email (EmailStr): A valid email address.
            plus (str): A string.
        """
        self.__email = email
        self.__plus = plus
        self.__token = None
        self._token_expiration = None

    def __str__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"<SolarPlusIntelbras {self.email}>"

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return self.__str__()

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
            str: The base API URL.
        """
        return self.__BASE_API_URL

    @property
    def token(self) -> str:
        """Returns the token. If the token is missing or expired, requests a new one.

        Returns:
            str: The token.
        """
        if not self.__token or self._is_token_expired():
            self._login()
        return self.__token

    def _is_token_expired(self) -> bool:
        """Checks if the token has expired by comparing the current time with the expiration time.

        Returns:
            bool: True if the token has expired, False otherwise.
        """
        if not self._token_expiration:
            return True
        return datetime.now(timezone.utc) >= self._token_expiration

    def _login(self) -> dict:
        """Faz a requisição de login, armazena o token e tempo de expiração.

        Returns:
            dict: A dictionary with the login response.
        """
        response = requests.post(
            f"{self.base_api_url}{EndpointEnum.LOGIN.value}",
            json={"email": self.email},
            headers={"plus": self.plus},
        )
        data = response.json()

        access_data = data["accessToken"]
        self.__token = access_data["accessJWT"]

        if "exp" in access_data:
            expires_ts = access_data["exp"]
            self._token_expiration = datetime.utcfromtimestamp(expires_ts).replace(
                tzinfo=timezone.utc
            )
        else:
            self._token_expiration = datetime.now(timezone.utc)

        return data
