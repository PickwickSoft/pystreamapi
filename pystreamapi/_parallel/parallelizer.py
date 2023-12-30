from joblib import Parallel as _JoblibParallel  # pylint: disable=unused-import

from pystreamapi._streams.error.__error import ErrorHandler
from pystreamapi._streams.error.__levels import ErrorLevel


class Parallel:
    """Wrapper for joblib.Parallel supporting error handling"""

    def __init__(self, n_jobs=-1, prefer="processes", handler: ErrorHandler = None):
        self.n_jobs = n_jobs
        self.prefer = prefer
        self.handler = handler

    def __call__(self, iterable):
        """Call joblib.Parallel with error handling"""
        res = _JoblibParallel(n_jobs=self.n_jobs, prefer=self.prefer)(iterable)
        if self.handler and self.handler._get_error_level() != ErrorLevel.RAISE:
            return ErrorHandler._remove_sentinel(res)
        return res
