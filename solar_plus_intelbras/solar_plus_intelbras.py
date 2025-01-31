from datetime import datetime, timezone

import requests
from pydantic import EmailStr

from solar_plus_intelbras.enums import EndpointEnum, KeyEnum, PeriodEnum


class SolarPlusIntelbras:
    """A class to represent a SolarPlusIntelbras."""

    __BASE_API_URL = "https://ens-server.intelbras.com.br/api/"

    def __init__(
        self,
        email: EmailStr,
        plus: str,
    ) -> None:
        """Construct a SolarPlusIntelbras object.

        Args:
            email (EmailStr): A valid email address.
            plus (str): A string.

        Returns:
            None: The constructor does not return anything.
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

    def plants(self) -> dict:
        """Return the plants.

        Returns:
            dict: A dictionary with the plants.
        """
        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
        )
        return response.json()

    def plants_detail(self, plant_id: int) -> dict:
        """Return the plant.

        Args:
            plant_id (int): A plant id.

        Returns:
            dict: A dictionary with the plants.
        """
        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
        )
        return response.json()

    def records(
        self,
        plant_id: int,
        period: PeriodEnum,
        key: KeyEnum,
        start_date: str,
        end_date: str,
    ) -> dict:
        """Return the records.

        Args:
            plant_id (int): A plant id.
            period (PeriodEnum): A period.
            key (KeyEnum): A key.
            start_date (str): A start date.
            end_date (str): An end date.

        Returns:
            dict: A dictionary with the records.
        """
        params = {
            "period": period,
            "key": key,
        }

        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            params["start_date"] = start_date
        except ValueError:
            raise ValueError("start_date must be in the format YYYY-MM-DD.")

        try:
            datetime.strptime(end_date, "%Y-%m-%d")
            params["end_date"] = end_date
        except ValueError:
            raise ValueError("end_date must be in the format YYYY-MM-DD.")

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}/{EndpointEnum.RECORDS.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()

    def records_year(
        self,
        year: int,
        plant_id: int,
    ) -> dict:
        """Return the records of a year.

        Args:
            year (int): A year.
            plant_id (int): A plant id.

        Returns:
            dict: A dictionary with the records.
        """
        params = {
            "key": KeyEnum.ENERGY_TODAY.value,
            "year": year,
            "period": PeriodEnum.YEAR.value,
        }

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}/{EndpointEnum.RECORDS_YEAR.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()

    def records_years(
        self,
        start_year: int,
        end_year: int,
        plant_id: int,
    ) -> dict:
        """Return the records of a year.

        Args:
            start_year (int): A year.
            end_year (int): A year.
            plant_id (int): A plant id.

        Returns:
            dict: A dictionary with the records.
        """

        params = {
            "start_year": start_year,
            "end_year": end_year,
            "key": KeyEnum.ENERGY_TODAY.value,
        }

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}/{EndpointEnum.RECORDS_YEARS.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()

    def inverters(self, plant_id: int, limit: int = 20, page: int = 1) -> dict:
        """Return the inverters.

        Args:
            limit (int): A limit.
            page (int): A page.

        Returns:
            dict: A dictionary with the inverters.
        """
        params = {"limit": limit, "page": page}

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}/{EndpointEnum.INVERTERS.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()

    def alerts(
        self,
        plant_id: int,
        start_date: str,
        end_date: str,
        limit: int = 20,
        page: int = 1,
    ) -> dict:
        """Return the alerts.

        Args:
            plant_id (int): A plant id.
            start_date (str): A start date.
            end_date (str): An end date.
            limit (int, optional): A limit. Defaults to 20.
            page (int, optional): A page. Defaults to 1.

        Returns:
            dict: A dictionary with the alerts.
        """
        params = {
            "limit": limit,
            "page": page,
        }

        if start_date:
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                params["start_date"] = start_date
            except ValueError:
                raise ValueError("start_date must be in the format YYYY-MM-DD.")

        if end_date:
            try:
                datetime.strptime(end_date, "%Y-%m-%d")
                params["end_date"] = end_date
            except ValueError:
                raise ValueError("end_date must be in the format YYYY-MM-DD.")

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}/{plant_id}/alerts",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()

    def notifications(
        self,
        start_date: str,
        end_date: str,
        pendings: bool = True,
        page: int = 1,
    ) -> dict:
        """Return the notifications.

        Args:
            start_date (str): A start date.
            end_date (str): An end date.
            pendings (bool, optional): A boolean. Defaults to True.
            page (int, optional): A page. Defaults to 1.

        Returns:
            dict: A dictionary with the notifications.
        """
        params = {
            "pendings": pendings,
            "page": page,
        }

        if start_date:
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                params["start_date"] = start_date
            except ValueError:
                raise ValueError("start_date must be in the format YYYY-MM-DD.")

        if end_date:
            try:
                datetime.strptime(end_date, "%Y-%m-%d")
                params["end_date"] = end_date
            except ValueError:
                raise ValueError("end_date must be in the format YYYY-MM-DD.")

        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.USER.value}/{EndpointEnum.NOTIFICATIONS.value}",
            headers={"Authorization": f"Bearer {self.token}", "plus": self.plus},
            params=params,
        )
        return response.json()
