import json
from pydantic import Field, PostgresDsn, ValidationError
from pydantic_settings import BaseSettings
from app.config.exception.exception import AppException

class Config(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = Field(..., description="Database connection string")
    FLASK_ENV: str = Field(..., description="Flask environment Variable ('development', 'production')")
    FLASK_DEBUG: bool = Field(default=False, description="Debug mode")
    SECRET_KEY: str = Field(..., description="Secret key")
    JWT_SECRET_KEY: str = Field(..., description="JWT secret key")
    SQLALCHEMY_TRACK_MODIFICATIONS:bool = Field(default=False, description="SQLAlchemy tracked modifications")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

try:
    appConfig = Config()
except ValidationError as e:
    errors = json.loads(e.json())
    formatted_errors = []
    for error in errors:
        field = ".".join(error['loc'])  # Get the field name
        message = error['msg']  # Get the error message
        formatted_errors.append(f"Error '{field}' is missing in .env: {message}")

    # Combine errors into a single exception message
    exception_message = "\n".join(formatted_errors)
    raise AppException(exception_message, 500) from None