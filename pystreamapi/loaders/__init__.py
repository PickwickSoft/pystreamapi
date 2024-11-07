__all__ = []

from pystreamapi.loaders.__csv.__csv_loader import csv
from pystreamapi.loaders.__json.__json_loader import json

__all__.append('csv')
__all__.append('json')

try:
    from pystreamapi.loaders.__xml.__xml_loader import xml

    __all__.append('xml')
except ImportError:
    ...

try:
    from pystreamapi.loaders.__yaml.__yaml_loader import yaml

    __all__.append('yaml')
except ImportError:
    ...
