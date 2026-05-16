from clients.base_client import BaseClient
from endpoints.auth_endpoint import AuthEndpoint

class AuthService(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoint_login = AuthEndpoint.LOGIN

    def auth(self, json):
        return self.post(self.endpoint_login, json)

    def profile(self, headers=None):
        return self.get(self.enpoint_profile, headers=headers)