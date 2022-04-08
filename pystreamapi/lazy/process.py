from typing import Callable


class Process:

    def __init__(self, work: Callable, arg):
        """
        The class representing a function to be executed lazy.
        :param work: the function or executable (normally with object)
        :param arg: the argument to be passed to the function
        """
        self.__work = work
        self.__arg = arg

    def exec(self):
        self.__work(self.__arg)
