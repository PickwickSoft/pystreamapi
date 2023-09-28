import json as jsonlib
from collections import namedtuple

from pystreamapi.loaders.__lazy_file_iterable import LazyFileIterable
from pystreamapi.loaders.__loader_utils import LoaderUtils


def json(src: str, read_from_src=False) -> LazyFileIterable:
    """
    Loads JSON data from either a path or a string and converts it into a list of namedtuples.

    Returns:
        list: A list of namedtuples, where each namedtuple represents an object in the JSON.
        :param src: Either the path to a JSON file or a JSON string.
        :param read_from_src: If True, src is treated as a JSON string. If False, src is treated as
        a path to a JSON file.
    """
    if read_from_src:
        return LazyFileIterable(lambda: __load_json_string(src))
    path = LoaderUtils.validate_path(src)
    return LazyFileIterable(lambda: __load_json_file(path))


def __load_json_file(file_path):
    """Load a JSON file and convert it into a list of namedtuples"""
    # skipcq: PTC-W6004
    with open(file_path, mode='r', encoding='utf-8') as jsonfile:
        src = jsonfile.read()
        if src == '':
            return []
        data = jsonlib.loads(src, object_hook=__dict_to_namedtuple)
    return data


def __load_json_string(json_string):
    """Load JSON data from a string and convert it into a list of namedtuples"""
    return jsonlib.loads(json_string, object_hook=__dict_to_namedtuple)


def __dict_to_namedtuple(d, name='Item'):
    """Convert a dictionary to a namedtuple"""
    if isinstance(d, dict):
        fields = list(d.keys())
        Item = namedtuple(name, fields)
        return Item(**{k: __dict_to_namedtuple(v, k) for k, v in d.items()})
    return d
