import secrets
from pydantic import BaseSettings



class Settings(BaseSettings):
    PROJECT_NAME: str = "project name"
    PORT: int = 8005
    HOST: str = '0.0.0.0'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    MONGO_CONNECTION_STRING: str = 'mongodb://docker:mongopw@localhost:55000'
    MONGO_COLLECTIONS: str = 'users'
    MONGO_DATABASE: str = 'myFirstDatabase'
    FIRST_SUPERUSER_NAME: str = 'dev'
    FIRST_SUPERUSER_EMAIL: str = 'me@example.com'
    FIRST_SUPERUSER_PASSWORD: str = 'dev'
    BACKEND_CORS_ORIGINS: list = []
    PUBLIC_FOLDER: str = 'public'


settings = Settings()
