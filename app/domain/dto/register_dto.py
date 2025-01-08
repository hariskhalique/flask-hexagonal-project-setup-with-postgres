from pydantic import BaseModel


class RegisterDTO(BaseModel):
    email: str
    password: str
    firstname: str
    lastname: str