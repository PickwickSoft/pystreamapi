from functools import reduce
from typing import Callable, Any, Iterable

from pystreamapi.lazy.process import Process
from pystreamapi.lazy.queue import ProcessQueue


class Stream:

    def __init__(self, source: Iterable):
        self.__source = list(source)
        self.__queue = ProcessQueue()

    def filter(self, function: Callable[[Any], bool]):
        self.__queue.append(Process(self.__filter, function))
        return self

    def __filter(self, function: Callable[[Any], bool]):
        self.__source = [element for element in self.__source if function(element)]

    def map(self, function: Callable[[Any], bool]):
        self.__queue.append(Process(self.__map, function))
        return self

    def __map(self, function: Callable[[Any], Any]):
        self.__source = [function(element) for element in self.__source]

    def reduce(self, function: Callable):
        self.__trigger_exec()
        return reduce(function, self.__source)

    def sorted(self):
        self.__trigger_exec()
        self.__source.sort()
        return self

    def for_each(self, function: Callable):
        self.__trigger_exec()
        self.__source = [function(element) for element in self.__source]

    def to_list(self):
        self.__trigger_exec()
        return self.__source

    def count(self):
        self.__trigger_exec()
        return len(self.__source)

    def __trigger_exec(self):
        self.__queue.execute_all()
