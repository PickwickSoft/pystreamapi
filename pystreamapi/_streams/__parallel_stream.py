from collections import defaultdict
from functools import reduce as seq_reduce
from typing import Callable, Any, Iterable

from joblib import delayed

import pystreamapi._streams.__base_stream as stream
from pystreamapi.__optional import Optional
from pystreamapi._parallel.fork_and_join import Parallelizer
from pystreamapi._parallel.parallelizer import Parallel
from pystreamapi._streams.__base_stream import terminal

_identity_missing = object()


class ParallelStream(stream.BaseStream):
    """The parallel implementation of BaseStream"""

    def __init__(self, source: Iterable[stream.K]):
        super().__init__(source)
        self._parallelizer = Parallelizer()

    def _init_parallelizer(self):
        self._parallelizer = Parallelizer()

    @terminal
    def all_match(self, predicate: Callable[[Any], bool]):
        return all(Parallel(n_jobs=-1, prefer="threads", handler=self)
                   (delayed(self.__mapper(predicate))(element) for element in self._source))

    def _filter(self, predicate: Callable[[Any], bool]):
        self._set_parallelizer_src()
        self._source = self._parallelizer.filter(predicate)

    @terminal
    def find_any(self):
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def _flat_map(self, predicate: Callable[[Any], stream.BaseStream]):
        new_src = []
        for element in Parallel(n_jobs=-1, prefer="threads", handler=self)(
                delayed(self.__mapper(predicate))(element) for element in self._source):
            new_src.extend(element.to_list())
        self._source = new_src

    def _group_to_dict(self, key_mapper: Callable[[Any], Any]):
        groups = defaultdict(list)

        def process_element(element):
            key = key_mapper(element)
            groups[key].append(element)

        Parallel(n_jobs=-1, prefer="threads", handler=self)(
            delayed(self.__mapper(process_element))(element) for element in self._source
        )
        return groups

    @terminal
    def for_each(self, action: Callable):
        self._peek(action)

    def _map(self, mapper: Callable[[Any], Any]):
        self._source = Parallel(n_jobs=-1, prefer="threads", handler=self)(
            delayed(self.__mapper(mapper))(element) for element in self._source
        )

    def _peek(self, action: Callable):
        Parallel(n_jobs=-1, prefer="threads", handler=self)(
            delayed(self.__mapper(action))(element) for element in self._source
        )

    @terminal
    def reduce(self, predicate: Callable[[Any, Any], Any], identity=_identity_missing,
               depends_on_state=False):
        self._set_parallelizer_src()
        reduce_func = seq_reduce if depends_on_state else self.__reduce
        if len(self._source) > 0:
            if identity is not _identity_missing:
                return reduce_func(predicate, self._source)
            return Optional.of(reduce_func(predicate, self._source))
        return identity if identity is not _identity_missing else Optional.empty()

    def __reduce(self, pred, _):
        return self._parallelizer.reduce(pred)

    @terminal
    def to_dict(self, key_mapper: Callable[[Any], Any]) -> dict:
        return dict(self._group_to_dict(key_mapper))

    def _set_parallelizer_src(self):
        self._parallelizer.set_source(self._source, self)

    def __mapper(self, mapper):
        return lambda x: self._one(mapper=mapper, item=x)
