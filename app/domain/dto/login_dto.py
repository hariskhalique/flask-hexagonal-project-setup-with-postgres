from pydantic import BaseModel, EmailStr, Field
from pydantic.v1 import validator


class LoginDto(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)


    @validator("password")
    def validate_password(self, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one number")
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter")
        return value