try:
    import yaml as yaml_lib
except ImportError as exc:
    raise ImportError(
        "Please install the yaml_loader extra dependency to use the yaml loader."
    ) from exc
from collections import namedtuple

from pystreamapi.loaders.__lazy_file_iterable import LazyFileIterable
from pystreamapi.loaders.__loader_utils import LoaderUtils


def yaml(src: str, read_from_src=False) -> LazyFileIterable:
    """
    Loads YAML data from either a path or a string and converts it into a list of namedtuples.

    Args:
        src (str): Either the path to a YAML file or a YAML string.
        read_from_src (bool): If True, src is treated as a YAML string. If False, src is treated as
            a path to a YAML file.

    Returns:
        list: A list of namedtuples, where each namedtuple represents an object in the YAML.
    """
    if read_from_src:
        return LazyFileIterable(lambda: __load_yaml_string(src))
    path = LoaderUtils.validate_path(src)
    return LazyFileIterable(lambda: __load_yaml_file(path))


def __load_yaml_file(file_path):
    """Load a YAML file and convert it into a list of namedtuples"""
    # skipcq: PTC-W6004
    with open(file_path, mode='r', encoding='utf-8') as yamlfile:
        src = yamlfile.read()
        if src == '':
            return []
        data = yaml_lib.safe_load(src)
        return __convert_to_namedtuples(data)


def __load_yaml_string(yaml_string):
    """Load YAML data from a string and convert it into a list of namedtuples"""
    data = yaml_lib.safe_load(yaml_string)
    return [] if data is None else __convert_to_namedtuples(data)


def __convert_to_namedtuples(data, name='Item'):
    """Convert YAML data to a list of namedtuples"""
    if isinstance(data, dict):
        fields = list(data.keys())
        Item = namedtuple(name, fields)
        return Item(**{k: __convert_to_namedtuples(v, k) for k, v in data.items()})
    if isinstance(data, list):
        return [__convert_to_namedtuples(item, name) for item in data]
    return data
