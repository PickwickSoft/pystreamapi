from typing import Callable, Any
from functools import reduce as seq_reduce
from joblib import Parallel, delayed
from optional import Optional

import pystreamapi.streams.__base_stream as stream
from pystreamapi.lazy.process import Process
from pystreamapi.parallel.itertools import reduce, pfilter

_identity_missing = object()


class ParallelStream(stream.BaseStream):
    """The parallel implementation of BaseStream"""

    def filter(self, predicate: Callable[[Any], bool]):
        self._queue.append(Process(self.__filter, predicate))
        return self

    def __filter(self, predicate: Callable[[Any], bool]):
        self._source = pfilter(self._source, predicate)

    def map(self, mapper: Callable[[Any], Any]):
        self._queue.append(Process(self.__map, mapper))
        return self

    def __map(self, predicate: Callable[[Any], Any]):
        self._source = Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                                             for element in self._source)

    def map_to_int(self):
        self._queue.append(Process(self.__map_to_int))
        return self

    def __map_to_int(self):
        self.__map(int)

    def map_to_str(self):
        self._queue.append(Process(self.__map_to_str))
        return self

    def __map_to_str(self):
        self.__map(str)

    def flat_map(self, predicate: Callable[[Any], stream.BaseStream]):
        self._queue.append(Process(self.__flat_map, predicate))
        return self

    def __flat_map(self, predicate: Callable[[Any], stream.BaseStream]):
        new_src = []
        for element in Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                                             for element in self._source):
            new_src.extend(element.to_list())
        self._source = new_src

    def peek(self, action: Callable):
        self._queue.append(Process(self.__peek, action))
        return self

    def __peek(self, predicate: Callable):
        Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                              for element in self._source)

    def reduce(self, predicate: Callable[[Any, Any], Any], identity=_identity_missing,
               depends_on_state=True):
        self._trigger_exec()
        reduce_func = reduce if depends_on_state is False else seq_reduce
        if len(self._source) > 0:
            if identity is not _identity_missing:
                return reduce_func(predicate, self._source)
            return Optional.of(reduce_func(predicate, self._source))
        return identity if identity is not _identity_missing else Optional.empty()

    def all_match(self, predicate: Callable[[Any], bool]):
        self._trigger_exec()
        return all(Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                                         for element in self._source))

    def find_any(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def for_each(self, predicate: Callable):
        self._trigger_exec()
        Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                              for element in self._source)
