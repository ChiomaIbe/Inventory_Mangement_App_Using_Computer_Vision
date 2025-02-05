from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application settings
    app_name: str = "Computer Vision Box Detection"
    api_version: str = "v1"
    debug: bool = True

    # Database settings (if applicable)
    # database_url: str

    # Edge Impulse model settings
    edge_impulse_project_id: str
    edge_impulse_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()