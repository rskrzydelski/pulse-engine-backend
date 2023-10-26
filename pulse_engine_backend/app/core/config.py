"""Config file."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""

    # DEBUG
    DEBUG: bool

    # PROJECT NAME, API PREFIX
    APP_ID: str = "pulse_engine_backend"
    PROJECT_NAME: str = "pulse_engine_backend"
    API_STR: str

    # UVICORN
    UVICORN_PORT_MAIN: int
    UVICORN_ADDRESS_MAIN: str

    class Config:
        """Config class."""

        env_file = ".env.test", ".env"
        case_sensitive = True


settings: Settings = Settings()
