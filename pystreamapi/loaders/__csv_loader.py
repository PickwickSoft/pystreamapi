import contextlib
from collections import namedtuple
from csv import reader


def csv(file_path: str, delimiter=',', encoding="utf-8") -> list:
    """
    Loads a CSV file and converts it into a list of namedtuples.

    Returns:
        list: A list of namedtuples, where each namedtuple represents a row in the CSV.
        :param encoding: The encoding of the CSV file.
        :param file_path: The path to the CSV file.
        :param delimiter: The delimiter used in the CSV file.
    """
    with open(file_path, 'r', newline='', encoding=encoding) as csvfile:
        csvreader = reader(csvfile, delimiter=delimiter)

        # Create a namedtuple type, casting the header values to int or float if possible
        Row = namedtuple('Row', list(next(csvreader)))

        # Process the data, casting values to int or float if possible
        data = [Row(*[__try_cast(value) for value in row]) for row in csvreader]

    return data

def __try_cast(value):
    """Try to cast value to primary data types from python (int, float, bool)"""
    for cast in (int, float):
        with contextlib.suppress(ValueError):
            return cast(value)
    # Try to cast to bool
    return value.lower() == 'true' if value.lower() in ('true', 'false') else value
