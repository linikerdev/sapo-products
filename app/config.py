import os
from typing import List, Type

from pydantic import BaseSettings

directoryDb = "/data_db"
basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    CONFIG_NAME: str = "base"
    USE_MOCK_EQUIVALENCY: bool = False
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class DevelopmentConfig(Settings):
    CONFIG_NAME: str = "dev"
    SECRET_KEY: str = os.getenv(
        "DEV_SECRET_KEY", "secret key application SAPO"
    )
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-dev.db".format(basedir)

def get_config(config):
    return config_by_name[config]

EXPORT_CONFIGS: List[Type[Settings]] = [
    DevelopmentConfig
]
config_by_name = {cfg().CONFIG_NAME: cfg() for cfg in EXPORT_CONFIGS}
