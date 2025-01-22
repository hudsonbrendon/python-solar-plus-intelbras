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
        """Return a string representation of the object."""
        return f"<SolarPlusIntelbras {self.email}>"

    def __repr__(self) -> str:
        """Return a string representation of the object."""
        return self.__str__()

    @property
    def email(self) -> EmailStr:
        """Return the email attribute."""
        return self.__email

    @property
    def plus(self) -> str:
        """Return the plus attribute."""
        return self.__plus

    @property
    def base_api_url(self) -> str:
        """Return the base_api_url attribute."""
        return self.__BASE_API_URL

    @property
    def token(self) -> str:
        """Retorna o token. Se o token estiver inexistente ou expirado, solicita um novo."""
        # Verifica se não temos token ou se ele já expirou
        if not self.__token or self._is_token_expired():
            self._login()  # Esse método vai atualizar self.__token e self._token_expiration
        return self.__token

    def _is_token_expired(self) -> bool:
        """Verifica se o token já expirou comparando a hora atual com a hora de expiração."""
        if not self._token_expiration:
            return True  # Se não houver registro de expiração, consideramos expirado
        return datetime.now(timezone.utc) >= self._token_expiration

    def _login(self) -> dict:
        """Faz a requisição de login, armazena o token e tempo de expiração."""
        response = requests.post(
            f"{self.base_api_url}{EndpointEnum.LOGIN.value}",
            json={"email": self.email},
            headers={"plus": self.plus},
        )
        data = response.json()

        # Aqui assumimos que o JSON de resposta contenha algo como:
        # {
        #   "accessToken": {
        #       "accessJWT": "...",
        #       "accessJWTExpiresAt": 1678045444,  # timestamp
        #       ...
        #   }
        # }

        access_data = data["accessToken"]
        self.__token = access_data["accessJWT"]

        # Se vier um timestamp de expiração, convertemos para datetime:
        if "exp" in access_data:
            expires_ts = access_data["exp"]
            self._token_expiration = datetime.utcfromtimestamp(expires_ts).replace(
                tzinfo=timezone.utc
            )
        else:
            # Se a API não retornar o tempo de expiração, você pode definir um tempo fixo ou tratar de outra forma.
            # Exemplo: 1 hora a partir de agora
            self._token_expiration = datetime.now(timezone.utc)

        return data

    def plants(self) -> dict:
        """Exemplo de utilização do token em outra chamada."""
        response = requests.get(
            f"{self.base_api_url}{EndpointEnum.PLANTS.value}",
            headers={
                "Authorization": f"Bearer {self.token}",
                "plus": self.plus,
            },
        )
        return response.json()
