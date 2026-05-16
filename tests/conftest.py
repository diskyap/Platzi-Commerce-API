import pytest
from services.auth_service import AuthService
from models.auth_model import AuthLoginRequest, AuthLoginResponse

@pytest.fixture(scope="session")
def auth_service():
    return AuthService()

@pytest.fixture(scope='session')
def accces_token(auth_service: AuthService):
     
    payload = AuthLoginRequest(
        email="john@mail.com",
        password="changeme",
    )

    response = auth_service.auth(payload.model_dump())
    auth_response = AuthLoginResponse(**response.json())
    return auth_response.access_token