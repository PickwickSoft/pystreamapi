from xml.etree import ElementTree
from collections import namedtuple
from pystreamapi.loaders.__lazy_file_iterable import LazyFileIterable
from pystreamapi.loaders.__loader_utils import LoaderUtils

__cast_types = True
__retrieve_children = True


def xml(src: str, read_from_src=False, retrieve_children=True, cast_types=True,
        encoding="utf-8") -> LazyFileIterable:
    """
    Loads XML data from either a path or a string and converts it into a list of namedtuples.
    Warning: This method isn't safe against malicious XML trees. Parse only safe XML from sources
    you trust.

    Returns:
        LazyFileIterable: A list of namedtuples, where each namedtuple represents an XML element.
        :param retrieve_children: If true, the children of the root element are used as stream elements.
        :param encoding: The encoding of the XML file.
        :param src: Either the path to an XML file or an XML string.
        :param read_from_src: If True, src is treated as an XML string. If False, src is treated as
            a path to an XML file.
        :param cast_types: Set as False to disable casting of values to int, bool or float.
    """
    global __cast_types, __retrieve_children
    __cast_types = cast_types
    __retrieve_children = retrieve_children
    if read_from_src:
        return LazyFileIterable(lambda: __load_xml_string(src))
    path = LoaderUtils.validate_path(src)
    return LazyFileIterable(lambda: __load_xml_file(path, encoding))


def __load_xml_file(file_path, encoding):
    """Load an XML file and convert it into a list of namedtuples."""
    with open(file_path, mode='r', encoding=encoding) as xmlfile:
        src = xmlfile.read()
        if not src:
            return []
        data = __parse_xml_string(src)
    return data


def __load_xml_string(xml_string):
    """Load XML data from a string and convert it into a list of namedtuples."""
    return __parse_xml_string(xml_string)


def __parse_xml_string(xml_string):
    """Parse XML string and convert it into a list of namedtuples."""
    root = ElementTree.fromstring(xml_string)
    parsed_xml = __parse_xml(root)
    return __flatten(parsed_xml) if __retrieve_children else [parsed_xml]


def __parse_xml(element):
    if len(element) == 0:
        return __parse_empty_element(element)
    elif len(element) == 1:
        return __parse_single_element(element)
    else:
        return __parse_multiple_elements(element)


def __parse_empty_element(element):
    return LoaderUtils.try_cast(element.text) if __cast_types else element.text


def __parse_single_element(element):
    sub_element = element[0]
    sub_item = __parse_xml(sub_element)
    Item = namedtuple(element.tag, [sub_element.tag])
    return Item(sub_item)


def __parse_multiple_elements(element):
    tag_dict = {}
    for e in element:
        if e.tag not in tag_dict:
            tag_dict[e.tag] = []
        tag_dict[e.tag].append(__parse_xml(e))
    filtered_dict = __filter_single_items(tag_dict)
    Item = namedtuple(element.tag, filtered_dict.keys())
    return Item(*filtered_dict.values())


def __filter_single_items(tag_dict):
    return {key: value[0] if len(value) == 1 else value for key, value in tag_dict.items()}


def __flatten(data):
    res = []
    for item in data:
        if isinstance(item, list):
            res.extend(item)
        else:
            res.append(item)
    return res
