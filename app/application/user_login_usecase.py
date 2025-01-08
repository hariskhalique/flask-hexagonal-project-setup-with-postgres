from flask_injector import inject
from pydantic import EmailStr

from app.domain.services.authenticate_service import AuthenticateService

class UserLoginUseCase:
    @inject
    def __init__(self, authentication: AuthenticateService):  # Explicit type annotation
        self.authentication = authentication

    def execute(self, email: EmailStr, password: str):
        """
        Execute the user login use case.
        """
        token = self.authentication.authenticate(email, password)
        return { 'token': token }