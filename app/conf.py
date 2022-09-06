import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '.env')
        )


settings = Settings()
