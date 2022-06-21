import logging.handlers
import os
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from constants.configurations import Logger

# from scripts.logging import LoggerUtil

_cnst_ = Logger()

if not os.path.exists(_cnst_.log_base_path):
    os.makedirs(_cnst_.log_base_path)

logging.trace = logging.DEBUG - 5
logging.addLevelName(logging.DEBUG - 5, 'TRACE')


class MaphisLogger(logging.getLoggerClass()):
    def __init__(self, name):
        super().__init__(name)

    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.trace):
            self._log(logging.trace, msg, args, **kwargs)


logging.setLoggerClass(MaphisLogger)

_logger = logging.getLogger("maphis")
_logger.setLevel(_cnst_.log_level)

if _cnst_.log_level == 'DEBUG' or _cnst_.log_level == 'TRACE':
    _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - '
                                   '%(lineno)d - %(message)s')
else:
    _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if 'file' in _cnst_.log_handlers:
    # Adding the log file handler to the logger
    _file_handler = logging.FileHandler(os.path.join(_cnst_.log_base_path, _cnst_.log_file_name))
    _file_handler.setFormatter(_formatter)
    _logger.addHandler(_file_handler)

if 'rotating' in _cnst_.log_handlers:
    # Adding the log file handler to the logger
    _rotating_file_handler = RotatingFileHandler(filename=os.path.join(_cnst_.log_base_path, _cnst_.log_file_name),
                                                 maxBytes=_cnst_.log_file_max_size,
                                                 backupCount=_cnst_.log_file_backup_count)
    _rotating_file_handler.setFormatter(_formatter)
    _logger.addHandler(_rotating_file_handler)

if 'console' in _cnst_.log_handlers:
    # Adding the log Console handler to the logger
    _console_handler = StreamHandler(sys.stdout)
    _console_handler.setFormatter(_formatter)
    _logger.addHandler(_console_handler)


def get_logger():
    return _logger
