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


class Logger:
    log_base_path = parser.get("LOG", "base_path", fallback='logs/')
    log_level = parser.get("LOG", "log_level", fallback='INFO')
    log_handlers = parser.get('LOG', 'handlers', fallback='rotating,console').split(',')
    log_file_name = parser.get('LOG', 'file_name', fallback='maphis-api-server.log')
    log_file_max_size = parser.getint('LOG', 'file_size_mb', fallback=100)
    log_file_backup_count = parser.getint('LOG', 'file_backup_count', fallback=10)
    log_enable_traceback = parser.getboolean('LOG', 'enable_traceback', fallback=False)


class Db:
    mongo_db_name = parser.get("DB", "mongo_db_name")
    mongo_db_host = parser.get("DB", "mongo_db_host", fallback="localhost").split(',')
    mongo_db_user = parser.get("DB", "mongo_db_user")
    mongo_db_password = parser.get("DB", "mongo_db_password")
    mongo_db_auth_db = parser.get("DB", "mongo_auth_db", fallback="admin")
