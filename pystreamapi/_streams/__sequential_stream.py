from collections import defaultdict
from typing import Callable, Any

import pystreamapi._streams.__base_stream as stream
from pystreamapi.__optional import Optional
from pystreamapi._streams.error.__error import _sentinel
from pystreamapi._itertools.tools import reduce

_identity_missing = object()


class SequentialStream(stream.BaseStream):
    """The sequential implementation of BaseStream"""

    @stream.terminal
    def all_match(self, predicate: Callable[[Any], bool]):
        return all(self._itr(self._source, mapper=predicate))

    def _filter(self, predicate: Callable[[Any], bool]):
        self._source = self._itr(self._source, condition=predicate)

    @stream.terminal
    def find_any(self):
        if len(self._source) > 0:
            return Optional.of(self._source[0])
        return Optional.empty()

    def _flat_map(self, predicate: Callable[[Any], stream.BaseStream]):
        new_src = []
        for element in self._itr(self._source, mapper=predicate):
            new_src.extend(element.to_list())
        self._source = new_src

    def _group_to_dict(self, key_mapper: Callable[[Any], Any]):
        groups = defaultdict(list)

        for element in self._source:
            key = self._one(mapper=key_mapper, item=element)
            if key == _sentinel:
                continue
            groups[key].append(element)
        return groups

    @stream.terminal
    def for_each(self, action: Callable):
        self._peek(action)

    def _map(self, mapper: Callable[[Any], Any]):
        self._source = self._itr(self._source, mapper=mapper)

    def _peek(self, action: Callable):
        self._itr(self._source, mapper=action)

    @stream.terminal
    def reduce(self, predicate: Callable, identity=_identity_missing, depends_on_state=False):
        if len(self._source) > 0:
            if identity is not _identity_missing:
                return reduce(predicate, self._source)
            return Optional.of(reduce(predicate, self._source, handler=self))
        return identity if identity is not _identity_missing else Optional.empty()

    @stream.terminal
    def to_dict(self, key_mapper: Callable[[Any], Any]) -> dict:
        return self._group_to_dict(key_mapper)
