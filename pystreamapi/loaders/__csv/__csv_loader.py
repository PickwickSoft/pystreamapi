from collections import namedtuple
from csv import reader

from pystreamapi.loaders.__loader_utils import LoaderUtils
from pystreamapi.loaders.__lazy_file_iterable import LazyFileIterable


def csv(file_path: str, cast_types=True, delimiter=',', encoding="utf-8") -> LazyFileIterable:
    """
    Loads a CSV file and converts it into a list of namedtuples.

    Returns:
        list: A list of namedtuples, where each namedtuple represents a row in the CSV.
        :param cast_types: Set as False to disable casting of values to int, bool or float.
        :param encoding: The encoding of the CSV file.
        :param file_path: The path to the CSV file.
        :param delimiter: The delimiter used in the CSV file.
    """
    file_path = LoaderUtils.validate_path(file_path)
    return LazyFileIterable(lambda: __load_csv(file_path, cast_types, delimiter, encoding))


def __load_csv(file_path, cast, delimiter, encoding):
    """Load a CSV file and convert it into a list of namedtuples"""
    # skipcq: PTC-W6004
    with open(file_path, mode='r', newline='', encoding=encoding) as csvfile:
        csvreader = reader(csvfile, delimiter=delimiter)

        # Create a namedtuple type, casting the header values to int or float if possible
        header = __get_csv_header(csvreader)

        Row = namedtuple('Row', list(header))

        mapper = LoaderUtils.try_cast if cast else lambda x: x

        # Process the data, casting values to int or float if possible
        data = [Row(*[mapper(value) for value in row]) for row in csvreader]
    return data


def __get_csv_header(csvreader):
    """Get the header of a CSV file. If the header is empty, return an empty list"""
    while True:
        try:
            header = next(csvreader)
            if header:
                break
        except StopIteration:
            return []
    return header
