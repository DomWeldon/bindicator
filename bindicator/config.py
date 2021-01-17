import typing

import pydantic


class Settings(pydantic.BaseSettings):
    MEROSS_EMAIL: str
    MEROSS_PASSWORD: str

    # url to query
    COUNCIL_URL: str
    # day of the week as locale full name (%A)
    BIN_DAY: str
    SENTRY_DSN: typing.Optional[str] = None


config = Settings()
