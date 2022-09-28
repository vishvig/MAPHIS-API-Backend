import os
import sys
from configparser import ConfigParser
from pydantic import BaseSettings

parser = ConfigParser()
parser.read(f"conf/application.conf")


class EnvironmentSettings(BaseSettings):
    SERVICE_HOST: str = parser.get("SERVICE", "host", fallback='localhost')
    SERVICE_PORT: int = int(parser.get("SERVICE", "port", fallback=5998))


env_settings = EnvironmentSettings(
    _env_file=".env", _env_file_encoding="utf-8"
)


class Service:
    port = env_settings.SERVICE_PORT
    host = env_settings.SERVICE_HOST
    images_path = parser.get("SERVICE", "images_path", fallback=os.path.join('assets', 'tiles'))


class Logger:
    log_base_path = parser.get("LOG", "base_path", fallback='logs/')
    log_level = parser.get("LOG", "log_level", fallback='INFO')
    log_handlers = parser.get('LOG', 'handlers', fallback='rotating,console').split(',')
    log_file_name = parser.get('LOG', 'file_name', fallback='maphis-api-server.log')
    log_file_max_size = parser.getint('LOG', 'file_size_mb', fallback=100)
    log_file_backup_count = parser.getint('LOG', 'file_backup_count', fallback=10)
    log_enable_traceback = parser.getboolean('LOG', 'enable_traceback', fallback=False)


class MongoDB:
    name = parser.get("MONGO", "name")
    host = parser.get("MONGO", "host", fallback="localhost").split(',')
    user = parser.get("MONGO", "user")
    password = parser.get("MONGO", "password")
    auth_db = parser.get("MONGO", "auth_db", fallback="admin")


class PostgresDB:
    name = parser.get("POSTGRES", "name")
    host = parser.get("POSTGRES", "host", fallback="localhost")
    port = parser.getint("POSTGRES", "port", fallback=5432)
    user = parser.get("POSTGRES", "user")
    password = parser.get("POSTGRES", "password")
    schema = parser.get("POSTGRES", "schema", fallback='v1')
    conn_str = f'postgresql://{user}:{password}@{host}:{port}/{name}'


class CacheDB:
    host = parser.get("CACHE", "host", fallback='localhost')
    port = parser.getint("CACHE", "port", fallback=6379)
    db_name = parser.getint("CACHE", "db", fallback=0)
