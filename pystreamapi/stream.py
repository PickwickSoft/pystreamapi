from functools import reduce
from typing import Callable, Any, Iterable


class Stream:

    def __init__(self, source: Iterable):
        self.__source = list(source)

    def filter(self, function: Callable[[Any], bool]):
        self.__source = [element for element in self.__source if function(element)]
        return self

    def map(self, function: Callable[[Any], Any]):
        self.__source = [function(element) for element in self.__source]
        return self

    def reduce(self, function: Callable):
        return reduce(function, self.__source)

    def sorted(self):
        self.__source.sort()
        return self

    def for_each(self, function: Callable):
        self.__source = [function(element) for element in self.__source]
        return self

    def to_list(self):
        return self.__source

    def count(self):
        return len(self.__source)
