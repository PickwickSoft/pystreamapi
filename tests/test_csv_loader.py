from unittest import TestCase
from unittest.mock import patch, mock_open

from pystreamapi.loaders import csv

file_content = """
attr1,attr2
1,2.0
a,b
"""


class TestCSVLoader(TestCase):

    def test_csv_loader(self):
        with patch('builtins.open', mock_open(read_data=file_content)):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.isfile', return_value=True):
                    data = csv('path/to/data.csv')
                    self.assertEqual(len(data), 2)
                    self.assertEqual(data[0].attr1, 1)
                    self.assertIsInstance(data[0].attr1, int)
                    self.assertEqual(data[0].attr2, 2.0)
                    self.assertIsInstance(data[0].attr2, float)
                    self.assertEqual(data[1].attr1, 'a')
                    self.assertIsInstance(data[1].attr1, str)

    def test_csv_loader_with_casting_disabled(self):
        with patch('builtins.open', mock_open(read_data=file_content)):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.isfile', return_value=True):
                    data = csv('path/to/data.csv', cast_types=False)
                    self.assertEqual(len(data), 2)
                    self.assertEqual(data[0].attr1, '1')
                    self.assertIsInstance(data[0].attr1, str)
                    self.assertEqual(data[0].attr2, '2.0')
                    self.assertIsInstance(data[0].attr2, str)
                    self.assertEqual(data[1].attr1, 'a')
                    self.assertIsInstance(data[1].attr1, str)

    def test_csv_loader_is_iterable(self):
        with patch('builtins.open', mock_open(read_data=file_content)):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.isfile', return_value=True):
                    data = csv('path/to/data.csv')
                    self.assertEqual(len(list(iter(data))), 2)

    def test_csv_loader_with_custom_delimiter(self):
        with patch('builtins.open', mock_open(read_data=file_content.replace(",", ";"))):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.isfile', return_value=True):
                    data = csv('path/to/data.csv', delimiter=';')
                    self.assertEqual(len(data), 2)
                    self.assertEqual(data[0].attr1, 1)
                    self.assertIsInstance(data[0].attr1, int)

    def test_csv_loader_with_empty_file(self):
        with patch('builtins.open', mock_open(read_data="")):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.isfile', return_value=True):
                    data = csv('path/to/data.csv')
                    self.assertEqual(len(data), 0)

    def test_csv_loader_with_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            csv('path/to/invalid.csv')

    def test_csv_loader_with_no_file(self):
        with self.assertRaises(ValueError):
            csv('./')
