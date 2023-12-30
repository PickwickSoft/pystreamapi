# pylint: disable=not-context-manager
from unittest import TestCase
from unittest.mock import patch, mock_open
from xml.etree.ElementTree import ParseError

from file_test import OPEN, PATH_EXISTS, PATH_ISFILE
from pystreamapi.loaders import xml

file_content = """
<employees>
    <employee>
        <name>John Doe</name>
        <salary>80000</salary>
    </employee>
    <employee>
        <name>Alice Smith</name>
        <child>
            <name>Frank</name>
        </child>
    </employee>
    <founder>
        <cars>
            <car>Bugatti</car>
            <car>Mercedes</car>
        </cars>
    </founder>
</employees>
"""
file_path = 'path/to/data.xml'


class TestXmlLoader(TestCase):

    def test_xml_loader_from_file_children(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = xml(file_path)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[0].salary, 80000)
            self.assertIsInstance(data[0].salary, int)
            self.assertEqual(data[1].child.name, "Frank")
            self.assertIsInstance(data[1].child.name, str)
            self.assertEqual(data[2].cars.car[0], 'Bugatti')
            self.assertIsInstance(data[2].cars.car[0], str)

    def test_xml_loader_from_file_no_children_false(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = xml(file_path, retrieve_children=False)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0].employee[0].salary, 80000)
            self.assertIsInstance(data[0].employee[0].salary, int)
            self.assertEqual(data[0].employee[1].child.name, "Frank")
            self.assertIsInstance(data[0].employee[1].child.name, str)
            self.assertEqual(data[0].founder.cars.car[0], 'Bugatti')
            self.assertIsInstance(data[0].founder.cars.car[0], str)

    def test_xml_loader_no_casting(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = xml(file_path, cast_types=False)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[0].salary, '80000')
            self.assertIsInstance(data[0].salary, str)
            self.assertEqual(data[1].child.name, "Frank")
            self.assertIsInstance(data[1].child.name, str)
            self.assertEqual(data[2].cars.car[0], 'Bugatti')
            self.assertIsInstance(data[2].cars.car[0], str)

    def test_xml_loader_is_iterable(self):
        with (patch(OPEN, mock_open(read_data=file_content)),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = xml(file_path)
            self.assertEqual(len(list(iter(data))), 3)

    def test_xml_loader_with_empty_file(self):
        with (patch(OPEN, mock_open(read_data="")),
              patch(PATH_EXISTS, return_value=True),
              patch(PATH_ISFILE, return_value=True)):
            data = xml(file_path)
            self.assertEqual(len(data), 0)

    def test_xml_loader_with_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            xml('path/to/invalid.xml')

    def test_xml_loader_with_no_file(self):
        with self.assertRaises(ValueError):
            xml('./')

    def test_xml_loader_from_string(self):
        data = xml(file_content, read_from_src=True)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0].salary, 80000)
        self.assertIsInstance(data[0].salary, int)
        self.assertEqual(data[1].child.name, "Frank")
        self.assertIsInstance(data[1].child.name, str)
        self.assertEqual(data[2].cars.car[0], 'Bugatti')
        self.assertIsInstance(data[2].cars.car[0], str)

    def test_xml_loader_from_empty_string(self):
        with self.assertRaises(ParseError):
            len(xml('', read_from_src=True))

    @patch('builtins.__import__', side_effect=ImportError('Mocked ImportError'))
    def test_defusedxml_not_installed(self, mock_import):
        with self.assertRaises(ImportError):
            from pystreamapi.loaders import xml
            xml(file_path)
