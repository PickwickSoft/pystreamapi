from __future__ import annotations

import logging

from pystreamapi._streams.error.__levels import ErrorLevel
from pystreamapi._streams.error.__sentinel import Sentinel

_sentinel = Sentinel()


def nothing(sth):
    """Do not modify the input"""
    return sth


def true_condition(_):
    """Always return True"""
    return True


class ErrorHandler:
    """Handle errors in stream operations"""

    __error_level = ErrorLevel.RAISE
    __exceptions_to_ignore = (Exception,)

    def _error_level(self, level: ErrorLevel, *exceptions):
        """
        Set the error level
        :param level: Error level from ErrorLevel
        :param exceptions: Exceptions to ignore. If not provided, all exceptions will be ignored
        """
        self.__exceptions_to_ignore = exceptions or (Exception,)
        self.__error_level = level

    def _get_error_level(self):
        """Get the error level"""
        return self.__error_level

    def _itr(self, src, mapper=nothing, condition=true_condition) -> list:
        """Iterate over the source and apply the mapper and condition"""
        new_src = []
        for i in src:
            try:
                if condition(i):
                    new_src.append(mapper(i))
            except self.__exceptions_to_ignore as e:
                if self.__error_level == ErrorLevel.RAISE:
                    raise e
                if self.__error_level == ErrorLevel.IGNORE:
                    continue
                self.__log(e)
        return new_src

    def _one(self, mapper=nothing, condition=true_condition, item=None):
        """
        Apply the mapper and condition to the item.
        If any exception occurs, handle it according to the error level
        (IGNORE, WARN: return _sentinel, RAISE: raise the exception)
        :param mapper: Method to apply to the item
        :param condition: Condition to check before applying the mapper
        :param item: Item to apply the mapper and condition
        :return: The result of the mapper if the condition is True, otherwise return _sentinel
        """
        try:
            if condition(item):
                return mapper(item)
        except self.__exceptions_to_ignore as e:
            if self.__error_level == ErrorLevel.RAISE:
                raise e
            if self.__error_level == ErrorLevel.IGNORE:
                return _sentinel
            self.__log(e)
        return _sentinel

    @staticmethod
    def _remove_sentinel(src: list):
        """Remove the sentinels from the list and its sublists"""
        result = []
        for item in src:
            if isinstance(item, list):
                # Recursively remove sentinel from sublist
                sublist = ErrorHandler._remove_sentinel(item)
                result.append(sublist)
            elif not isinstance(item, Sentinel):
                result.append(item)
        return result

    @staticmethod
    def __log(exception: Exception):
        """Log the exception"""
        logging.warning("An exception has been ignored: %s", exception)
