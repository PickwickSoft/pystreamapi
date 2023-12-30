# pylint: disable=not-context-manager
from json import JSONDecodeError
from unittest import TestCase
from unittest.mock import patch, mock_open

from _loaders.file_test import OPEN, PATH_EXISTS, PATH_ISFILE
from pystreamapi.loaders import json

file_content = """
[
    {
        "attr1": 1,
        "attr2": 2.0
    },
    {
        "attr1": "a",
        "attr2": "b"
    }
]
"""
file_path = 'path/to/data.json'

class TestJsonLoader(TestCase):

    def test_json_loader_from_file(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = json(file_path)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0].attr1, 1)
            self.assertIsInstance(data[0].attr1, int)
            self.assertEqual(data[0].attr2, 2.0)
            self.assertIsInstance(data[0].attr2, float)
            self.assertEqual(data[1].attr1, 'a')
            self.assertIsInstance(data[1].attr1, str)

    def test_json_loader_is_iterable(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = json(file_path)
            self.assertEqual(len(list(iter(data))), 2)

    def test_json_loader_with_empty_file(self):
        with (patch(OPEN, mock_open(read_data="")),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = json(file_path)
            self.assertEqual(len(data), 0)

    def test_json_loader_with_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            json('path/to/invalid.json')

    def test_json_loader_with_no_file(self):
        with self.assertRaises(ValueError):
            json('../')

    def test_json_loader_from_string(self):
        data = json(file_content, read_from_src=True)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0].attr1, 1)
        self.assertIsInstance(data[0].attr1, int)
        self.assertEqual(data[0].attr2, 2.0)
        self.assertIsInstance(data[0].attr2, float)
        self.assertEqual(data[1].attr1, 'a')
        self.assertIsInstance(data[1].attr1, str)

    def test_json_loader_from_empty_string(self):
        with self.assertRaises(JSONDecodeError):
            len(json('', read_from_src=True))
