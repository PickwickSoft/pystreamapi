# Data Loaders

Data loaders provide a convenient way to process data from various data files in your streams. You can access the values of each data set as if it were an object, containing the header names as attributes.

{% hint style="info" %}
Currently, PyStreamAPI only supports reading data from CSV files.
{% endhint %}

To use the loaders, you can import them with this line:

```python
from pystreamapi.loaders import ...
```

### CSV loader

In order to load the data from a CSV file, you can use the `csv` loader.

You just need the file's path, and you can optionally specify the delimiter and the encoding. By default, the encoding is set to UTF-8.&#x20;

By default, all values get converted to `int`, `float`, `bool` or otherwise `str`.

The example below uses this CSV file:

{% code title="data.csv" fullWidth="false" %}
```csv
name;age
Joe;20
Jane;30
John;78
```
{% endcode %}

```python
from pystreamapi.loaders import csv

Stream.of(csv("path/to/data.csv", delimiter=";", encoding="us-ascii")) \
    .map(lambda x: x.name) \
    .for_each(print) # "Joe", "Jane", "John"
```
