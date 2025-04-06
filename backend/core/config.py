from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv


load_dotenv()

class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 80


class ApiV1Prefix(BaseModel):
    prefix: str = '/v1'
    users: str = '/users'


class ApiPrefix(BaseModel):
    prefix: str = '/api'
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = os.environ.get('ECHO')
    echo_pool: bool = os.environ.get("ECHO_POOL")
    pool_size: int = os.environ.get("POOL_SIZE")
    max_overflow: int = os.environ.get("MAX_OVERFLOW")

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="AGB_APP__"
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
print(settings.db.url)