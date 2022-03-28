import time
import uuid
import random
from copy import deepcopy

from datetime import datetime, timezone
from scripts.logging.logger import get_logger
from scripts.constants.constants import CommonConstants

LOG = get_logger()


class CommonUtils(object):
    def __init__(self):
        self._cnst_ = CommonConstants()

    @staticmethod
    def get_utc_datetime_now():
        return datetime.utcnow()

    def ui_datetime_format(self):
        return self._cnst_.ui

    def utc_datetime_format(self):
        return self._cnst_.utc

    def nsc_datetime_format(self):
        return self._cnst_.nsc

    def get_datetime_str(self, dt=None, dt_format='utc'):
        """
        Returns the datetime string.
        :param dt: The datetime value to be converted as str. If None, Current UTC time will be returned.
        :param dt_format: The format to which the date string should be converted. 'utc_datetime_format' is the default.
                Supported values are:- 'ui', 'utc', 'nsc'
        :return: Datetime string
        """
        dt_format_str = f"{dt_format}_datetime_format"
        if dt is None:
            dt = self.get_utc_datetime_now()
        return dt.strftime(getattr(self, dt_format_str)())

    def get_datetime_dt(self, dt_str=None, dt_format='utc'):
        """
        Returns the datetime object.
        :param dt_str: The datetime string to be converted as object. If None, Current UTC time will be returned.
        :param dt_format: The format to which the date string should be converted. 'utc_datetime_format' is the default.
                Supported values are:- 'ui', 'utc', 'nsc'
        :return: Datetime object
        """
        dt_format_str = f"{dt_format}_datetime_format"
        if dt_str is None:
            return self.get_utc_datetime_now()
        return datetime.strptime(dt_str, getattr(self, dt_format_str)())

    @staticmethod
    def get_epoch_now(_round=True):
        if _round:
            return int(time.time())
        else:
            return time.time()

    @staticmethod
    def system_timezone():
        return datetime.now(timezone.utc).astimezone().tzname()

    @staticmethod
    def local_time_offset(t=None):
        if t is None:
            t = time.time()

        if time.localtime(t).tm_isdst and time.daylight:
            return -time.altzone
        else:
            return -time.timezone

    def tz_offset_hm(self):
        seconds = self.local_time_offset()
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)

    @staticmethod
    def epoch_to_datetime(epoch):
        if epoch is None:
            return None
        return datetime.fromtimestamp(epoch)

    @staticmethod
    def deep_copy(_input):
        return deepcopy(_input)

    @staticmethod
    def random_choice(_input=None):
        if _input is None:
            return None
        return random.choice(_input)

    @staticmethod
    def generate_random_id():
        return uuid.uuid4().hex
