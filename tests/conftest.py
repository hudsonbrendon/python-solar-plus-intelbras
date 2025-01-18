import pytest

from solar_plus_intelbras.solar_plus_intelbras import SolarPlusIntelbras


@pytest.fixture
def solar_plus_intelbras() -> SolarPlusIntelbras:
    return SolarPlusIntelbras("test@email.com", "test")


@pytest.fixture
def login_response() -> dict:
    return {
        "user": {
            "id": 6851,
            "email": "test@email.com",
            "name": "Test",
            "cpf": "",
            "picture": "",
            "preferences": {
                "currency": "BRL",
                "timezone": "-3",
                "temperatureUnit": "c",
                "sendWeatherNotification": True,
                "sendEnergyTodayNotification": True,
                "sendAlertNotification": True,
            },
        },
        "accessToken": {
            "exp": 1737175716,
            "expAt": "2025-01-18 01:48:36",
            "iat": 1737175416,
            "accessJWT": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InBpY3R1cmUiOiIiLCJpZCI6Njg1MSwiZW1haWwiOiJjb250YXRvLmh1ZHNvbmJyZW5kb25AZ21haWwuY29tIiwibmFtZSI6Ikh1ZHNvbiBCcmVuZG9uIiwiY3BmIjoiIiwicGhvbmUiOiIiLCJjcmVhdGVkQXQiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYxMDY5OC0wMzowMCIsImFjdGl2YXRlZEF0Ijp7IlRpbWUiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYwODEwNS0wMzowMCIsIlZhbGlkIjp0cnVlfSwibGFzdExvZ2luIjoiMjAyNS0wMS0xNyAyMzoyNToxNC4zOTAwMjg0MzYgLTAzMDAgLTAzIG09KzUyMzkyLjQ4ODc5MjE1MSIsInByZWZlcmVuY2VzIjp7ImN1cnJlbmN5IjoiQlJMIiwidGltZXpvbmUiOiItMyIsInRlbXBlcmF0dXJlVW5pdCI6ImMiLCJzZW5kV2VhdGhlck5vdGlmaWNhdGlvbiI6dHJ1ZSwic2VuZEVuZXJneVRvZGF5Tm90aWZpY2F0aW9uIjp0cnVlLCJzZW5kQWxlcnROb3RpZmljYXRpb24iOnRydWV9LCJyZWdpc3RyYXRpb25Ub2tlbiI6ImQxbWNVRzNVSjA5UHN3d0JDLXVFUDk6QVBBOTFiRzJ4Z3dXUDIzVFhab0tiejVIamZpQW9EbnIxeGEtT1haVTZDMXVEQWIyczZPU3NkRHdMQ3VYTWxkdnBYM0ZJcF9jQloxRU4zU2xsZm5nWmVCYU1aNUNsLWhvcGNLajNhWnRWTTE0MEsyT1U4Tno3eHMiLCJhY3RpdmF0aW9uQ29kZSI6ImU2YjE2OGRkZjc0M2QwOWE4OGU2NmYwZWZhMDZiMDE1In0sImV4cCI6MTczNzE3NTcxNiwiaWF0IjoxNzM3MTc1NDE2LCJjb2RlIjoiIiwicm9sZSI6ImNsaWVudCJ9.FXOp76WgRRemmiOr2z4ML6QVEG1fbDYk1LfYK_hm3vs",
        },
        "refreshToken": {
            "exp": 1737261816,
            "expAt": "2025-01-19 01:43:36",
            "iat": 1737175416,
            "refreshJWT": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InBpY3R1cmUiOiIiLCJpZCI6Njg1MSwiZW1haWwiOiJjb250YXRvLmh1ZHNvbmJyZW5kb25AZ21haWwuY29tIiwibmFtZSI6Ikh1ZHNvbiBCcmVuZG9uIiwiY3BmIjoiIiwicGhvbmUiOiIiLCJjcmVhdGVkQXQiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYxMDY5OC0wMzowMCIsImFjdGl2YXRlZEF0Ijp7IlRpbWUiOiIyMDI0LTEyLTE2VDE0OjQ5OjU2LjYwODEwNS0wMzowMCIsIlZhbGlkIjp0cnVlfSwibGFzdExvZ2luIjoiMjAyNS0wMS0xNyAyMzoyNToxNC4zOTAwMjg0MzYgLTAzMDAgLTAzIG09KzUyMzkyLjQ4ODc5MjE1MSIsInByZWZlcmVuY2VzIjp7ImN1cnJlbmN5IjoiQlJMIiwidGltZXpvbmUiOiItMyIsInRlbXBlcmF0dXJlVW5pdCI6ImMiLCJzZW5kV2VhdGhlck5vdGlmaWNhdGlvbiI6dHJ1ZSwic2VuZEVuZXJneVRvZGF5Tm90aWZpY2F0aW9uIjp0cnVlLCJzZW5kQWxlcnROb3RpZmljYXRpb24iOnRydWV9LCJyZWdpc3RyYXRpb25Ub2tlbiI6ImQxbWNVRzNVSjA5UHN3d0JDLXVFUDk6QVBBOTFiRzJ4Z3dXUDIzVFhab0tiejVIamZpQW9EbnIxeGEtT1haVTZDMXVEQWIyczZPU3NkRHdMQ3VYTWxkdnBYM0ZJcF9jQloxRU4zU2xsZm5nWmVCYU1aNUNsLWhvcGNLajNhWnRWTTE0MEsyT1U4Tno3eHMiLCJhY3RpdmF0aW9uQ29kZSI6ImU2YjE2OGRkZjc0M2QwOWE4OGU2NmYwZWZhMDZiMDE1In0sImV4cCI6MTczNzI2MTgxNiwiaWF0IjoxNzM3MTc1NDE2LCJjb2RlIjoiIiwicm9sZSI6ImNsaWVudCJ9.Y6JFTXgrcc-SD1nYutJj8kwUVvFgS8YaGDLMavNA7V4",
        },
        "accessTokenContaUnica": "",
        "refreshTokenContaUnica": "",
        "loginType": "code",
        "requestIP": "187.19.163.111",
        "registrationToken": "",
        "code": "",
        "role": "client",
        "businessAccount": {
            "id": 0,
            "createdAt": "0001-01-01T00:00:00Z",
            "updatedAt": "0001-01-01T00:00:00Z",
            "userOwnerID": 0,
            "userOwner": {
                "id": 0,
                "createdAt": "0001-01-01T00:00:00Z",
                "updatedAt": "0001-01-01T00:00:00Z",
                "lastLogin": "",
                "email": "",
                "clientID": "",
                "clientSecret": "",
                "picture": "",
                "registrationToken": "",
                "passwordRecoveryCode": "",
                "passwordRecoveryExpiresAt": {
                    "Time": "0001-01-01T00:00:00Z",
                    "Valid": False,
                },
                "name": "",
                "cpf": "",
                "phone": "",
                "activationCode": "",
                "activatedAt": {"Time": "0001-01-01T00:00:00Z", "Valid": False},
                "sessions": None,
                "pushesNotification": None,
                "preferences": {
                    "sendWeatherNotification": None,
                    "sendEnergyTodayNotification": None,
                    "sendAlertNotification": None,
                },
            },
            "name": "",
            "code": "",
            "cnpj": "",
            "webSite": "",
            "phone": "",
        },
    }
