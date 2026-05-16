# Standard library
import json

# Third-party
import allure
import pytest
from assertpy import assert_that
from jsonschema import validate

# Local imports
from models.auth_model import (
    AuthLoginRequest,
    AuthLoginResponse,
    AuthLoginResponseInvalid
)

from schemas.auth_schema import AUTH_VALID_SCHEMA, AUTH_INVALID_SCHEMA
from services.auth_service import AuthService
from utils.file_reader import load_test_data

VALID_LOGIN_DATA = load_test_data("login_valid.json")
INVALID_LOGIN_DATA = load_test_data("login_invalid.json")

@allure.feature("Authentication")
@allure.story("Login API")
@allure.severity(allure.severity_level.CRITICAL)

class TestAuthApi:
    
    @pytest.mark.positive
    @pytest.mark.parametrize("email, password, expected_status, test_id", 
        VALID_LOGIN_DATA,
        ids=[data[3] for data in VALID_LOGIN_DATA]
    )
    def test_auth_login_success(self, auth_service: AuthService, email, password, expected_status, test_id):

        allure.dynamic.title(f"Login Test - {test_id}")

        payload = AuthLoginRequest(email=email, password=password)

        with allure.step("Send login request"):
            response = auth_service.auth(payload.model_dump())
            response_json = response.json()

        with allure.step("Validate response status code"):
            assert_that(response.status_code).is_equal_to(expected_status)

        with allure.step("Validate response body"):
            assert_that(response_json).contains_key("access_token")
            assert_that(response_json["access_token"]).starts_with("ey")
            assert_that(response_json["refresh_token"]).starts_with("ey")

        with allure.step("Validate response schema"):
            AuthLoginResponse(**response_json)
            validate(
                instance=response_json,
                schema=AUTH_VALID_SCHEMA
            )

        with allure.step("Attach login request payload"):
            allure.attach(
                json.dumps(payload.model_dump(), indent=4),
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Attach login response payload"):

            response_body = response_json.copy()

            for token in ["access_token", "refresh_token"]:
                if token in response_body:
                    response_body[token] = "***masked***"
            
            allure.attach(
                json.dumps(response_body, indent=4),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )
    
    @pytest.mark.negative
    @pytest.mark.parametrize("email, password, expected_status, test_id", 
        INVALID_LOGIN_DATA,
        ids=[data[3] for data in INVALID_LOGIN_DATA]
    )
    def test_auth_login_invalid(self, auth_service: AuthService, email, password, expected_status, test_id):

        allure.dynamic.title(f"Login Test - {test_id}")

        payload = AuthLoginRequest(email=email, password=password)

        with allure.step("Send login request"):
            response = auth_service.auth(payload.model_dump())
            response_json = response.json()

        with allure.step("Validate response status code"):
            assert_that(response.status_code).is_equal_to(expected_status)

        with allure.step("Validate response body"):
            assert_that(response_json).contains_key("message")
            assert_that(response_json["message"]).is_equal_to("Unauthorized")

        with allure.step("Validate response schema"):
            AuthLoginResponseInvalid(**response_json)
            validate(
                instance=response_json,
                schema=AUTH_INVALID_SCHEMA
            )

        with allure.step("Attach login request payload"):
            allure.attach(
                json.dumps(payload.model_dump(), indent=4),
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Attach login response payload"):

            response_body = response_json.copy()

            for token in ["access_token", "refresh_token"]:
                if token in response_body:
                    response_body[token] = "***masked***"
            
            allure.attach(
                json.dumps(response_body, indent=4),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )