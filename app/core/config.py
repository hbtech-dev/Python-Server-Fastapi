from typing import List, Union
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Backend Server"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A professional FastAPI backend server with clean architecture"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    BACKEND_CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:5173",
    ]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    DATABASE_URL: str = "sqlite:///./app.db"
    
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = ""
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAILS_FROM_EMAIL: str = ""
    EMAILS_FROM_NAME: str = PROJECT_NAME
    
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
