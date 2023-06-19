from functools import reduce as seq_reduce
from typing import Callable, Any, Iterable

from joblib import Parallel, delayed
from optional import Optional

import pystreamapi._streams.__base_stream as stream
from pystreamapi._parallel.fork_and_join import Parallelizer

_identity_missing = object()


class ParallelStream(stream.BaseStream):
    """The parallel implementation of BaseStream"""

    def __init__(self, source: Iterable[stream.K]):
        super().__init__(source)
        self.parallelizer = Parallelizer()

    def all_match(self, predicate: Callable[[Any], bool]):
        self._trigger_exec()
        return all(Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                                         for element in self._source))

    def _filter(self, predicate: Callable[[Any], bool]):
        self._set_parallelizer_src()
        self._source = self.parallelizer.filter(predicate)

    def find_any(self):
        self._trigger_exec()
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def _flat_map(self, predicate: Callable[[Any], stream.BaseStream]):
        new_src = []
        for element in Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                                             for element in self._source):
            new_src.extend(element.to_list())
        self._source = new_src

    def _group_to_dict(self, key_mapper: Callable[[Any], Any]):
        groups = {}

        def process_element(element):
            key = key_mapper(element)
            if key not in groups:
                groups[key] = []
            groups[key].append(element)

        Parallel(n_jobs=-1, prefer="threads")(delayed(process_element)(element)
                                              for element in self._source)
        return groups

    def for_each(self, predicate: Callable):
        self._trigger_exec()
        Parallel(n_jobs=-1, prefer="threads")(delayed(predicate)(element)
                                              for element in self._source)

    def _map(self, mapper: Callable[[Any], Any]):
        self._source = Parallel(n_jobs=-1, prefer="threads")(delayed(mapper)(element)
                                                             for element in self._source)

    def _peek(self, action: Callable):
        Parallel(n_jobs=-1, prefer="threads")(delayed(action)(element)
                                              for element in self._source)

    def reduce(self, predicate: Callable[[Any, Any], Any], identity=_identity_missing,
               depends_on_state=False):
        self._trigger_exec()
        self._set_parallelizer_src()
        reduce_func = seq_reduce if depends_on_state else self.__reduce
        if len(self._source) > 0:
            if identity is not _identity_missing:
                return reduce_func(predicate, self._source)
            return Optional.of(reduce_func(predicate, self._source))
        return identity if identity is not _identity_missing else Optional.empty()

    def __reduce(self, pred, _):
        return self.parallelizer.reduce(pred)

    def to_dict(self, key_mapper: Callable[[Any], Any]) -> dict:
        self._trigger_exec()
        return dict(self._group_to_dict(key_mapper))

    def _set_parallelizer_src(self):
        self.parallelizer.set_source(self._source)
