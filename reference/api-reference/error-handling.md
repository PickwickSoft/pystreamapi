---
description: Work with data that you don't know
---

# Error handling

PyStreamAPI offers a powerful error handling mechanism that allows you to handle errors in a declarative manner. This is especially useful when working with data that you don't know.

PyStreamAPI offers three different error levels:

* `ErrorLevel.RAISE`: This is the default error level. It will raise an exception if an error occurs.
* `ErrorLevel.IGNORE`: This error level will ignore any errors that occur and won't inform you.
* `ErrorLevel.WARN`: This error level will warn you about any errors that occur and logs them as a warning with default logger.

You can change the error by using the `error_level(...)` method. All operations following it will use the new level.

```python
from pystreamapi import Stream, ErrorLevel

Stream.of([" ", '3', None, "2", 1, ""]) \
    .error_level(ErrorLevel.IGNORE) \
    .map_to_int() \
    .error_level(ErrorLevel.RAISE) \
    .sorted() \
    .for_each(print) # Output: 1 2 3
```

The code above will ignore all errors that occur during mapping to int and will just skip the elements.

For more details on how to use error handling, please refer to the documentation.

{% hint style="warning" %}
Do not use `ErrorLevel.IGNORE` if you know how to filter out the errors. This could result in unexpected behavior and is against the principles of functional programming.

Error handling is only meant to be used to handle unknown data and it is not intended to be used as a replacement for filtering and proper data validation.
{% endhint %}

Here is an example on how/why you should not use it to replace filtering:

```python
from pystreamapi import Stream, ErrorLevel

class Alien:
    def __int__(self):
        # You never know what the implementation of int() does
        return 1 # You probably do not expect aliens to be represented as int!

print(Stream.of([" ", '3', None, "2", 1, "", Alien()]) \
    .error_level(ErrorLevel.IGNORE) \
    .map_to_int() \
    .sorted() \
    .reduce(lambda x, y: x+y).get()) # Output: 7, not 6 as you might expect
```
