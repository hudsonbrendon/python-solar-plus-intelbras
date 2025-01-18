from pydantic import EmailStr


class SolarPlusIntelbras:
    def __init__(self, email: EmailStr, plus: str) -> None:
        self.__email = email
        self.__plus = plus

    @property
    def email(self) -> EmailStr:
        return self.__email

    @property
    def plus(self) -> str:
        return self.__plus

    def __str__(self) -> str:
        return f"<SolarPlusIntelbras {self.email}>"

    def __repr__(self) -> str:
        return self.__str__()
