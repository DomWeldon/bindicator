import pydantic


class Settings(pydantic.BaseSettings):
    MEROSS_EMAIL: str
    MEROSS_PASSWORD: str


config = Settings()
