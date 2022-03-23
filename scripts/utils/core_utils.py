from scripts.constants.configurations import Logger


class CoreUtils(object):
    def __init__(self):
        self._lc_ = Logger

    @staticmethod
    def api_sandbox_str(sandbox=False):
        return "-sandbox" if sandbox is True else ""

    def enable_traceback(self):
        return self._lc_.log_enable_traceback
